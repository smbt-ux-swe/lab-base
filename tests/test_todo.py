"""
Week 7 Lab Tests — do not modify.

Run with: pytest tests/ -v

Before you start:  TestInMemoryAPI → PASS, everything else → FAIL
After you finish:  ALL tests → PASS
"""


class TestInMemoryAPI:
    """These should PASS immediately — the starter API already works."""

    def test_get_all_todos(self, client):
        r = client.get('/api/todos')
        assert r.status_code == 200

    def test_get_single_todo(self, client):
        client.post('/api/todos', json={"title": "Test"})
        r = client.get('/api/todos/1')
        assert r.status_code == 200

    def test_create_todo(self, client):
        r = client.post('/api/todos', json={"title": "Test todo"})
        assert r.status_code == 201
        assert r.get_json()['title'] == "Test todo"

    def test_create_todo_missing_title(self, client):
        r = client.post('/api/todos', json={"description": "No title"})
        assert r.status_code == 400


class TestSQLAlchemySetup:
    """FAIL until TODO 1 + TODO 2 are done."""

    def test_db_instance(self, client):
        """app.py should export a 'db' SQLAlchemy instance."""
        try:
            from app import db
            assert db is not None
        except ImportError:
            assert False, "Cannot import 'db' from app — complete TODO 1"

    def test_todo_model_exists(self, client):
        """app.py should export a 'TodoModel' class."""
        try:
            from app import TodoModel
            assert TodoModel is not None
        except ImportError:
            assert False, "Cannot import 'TodoModel' from app — complete TODO 2"

    def test_todo_model_tablename(self, client):
        """TodoModel.__tablename__ should be 'todos'."""
        from app import TodoModel
        assert TodoModel.__tablename__ == "todos"

    def test_todo_model_columns(self, client):
        """TodoModel should have id, title, description, status, priority columns."""
        from app import TodoModel
        cols = [c.name for c in TodoModel.__table__.columns]
        for col in ['id', 'title', 'description', 'status', 'priority']:
            assert col in cols, f"TodoModel missing '{col}' column"

    def test_todo_model_to_dict(self, client):
        """TodoModel.to_dict() should return all fields as a dictionary."""
        from app import TodoModel
        todo = TodoModel(title="Test", description="Desc", status="pending", priority="high")
        d = todo.to_dict()
        assert d['title'] == "Test"
        assert d['description'] == "Desc"
        assert d['status'] == "pending"
        assert d['priority'] == "high"

    def test_title_not_nullable(self, client):
        """TodoModel.title should be nullable=False."""
        from app import TodoModel
        title_col = TodoModel.__table__.columns['title']
        assert title_col.nullable is False, "title column should have nullable=False"


class TestPersistentCRUD:
    """FAIL until TODO 3 + TODO 4 are done."""

    def test_database_starts_empty(self, client):
        """
        After switching to SQLAlchemy, GET /api/todos should return []
        because the test uses a fresh in-memory database.
        If this returns the hardcoded list, the routes still use the list.
        """
        r = client.get('/api/todos')
        data = r.get_json()
        assert data == [], \
            f"Expected empty list from fresh database, got {len(data)} items — routes still using in-memory list?"

    def test_create_and_retrieve(self, client):
        """Create a todo via POST, then retrieve it via GET."""
        r = client.post('/api/todos', json={
            "title": "Persistent todo",
            "description": "Should be in the database",
            "priority": "high"
        })
        assert r.status_code == 201
        todo_id = r.get_json()['id']

        r = client.get(f'/api/todos/{todo_id}')
        assert r.status_code == 200
        assert r.get_json()['title'] == "Persistent todo"
        assert r.get_json()['priority'] == "high"

    def test_create_defaults(self, client):
        """Creating with only title should default status=pending, priority=medium."""
        r = client.post('/api/todos', json={"title": "Minimal"})
        assert r.status_code == 201
        data = r.get_json()
        assert data['status'] == "pending"
        assert data['priority'] == "medium"

    def test_update(self, client):
        """Create then update a todo."""
        r = client.post('/api/todos', json={"title": "Before"})
        todo_id = r.get_json()['id']

        r = client.put(f'/api/todos/{todo_id}', json={
            "title": "After",
            "status": "done"
        })
        assert r.status_code == 200
        assert r.get_json()['title'] == "After"
        assert r.get_json()['status'] == "done"

    def test_delete(self, client):
        """Create then delete a todo."""
        r = client.post('/api/todos', json={"title": "Delete me"})
        todo_id = r.get_json()['id']

        r = client.delete(f'/api/todos/{todo_id}')
        assert r.status_code == 200

        r = client.get(f'/api/todos/{todo_id}')
        assert r.status_code == 404

    def test_filter_by_status(self, client):
        """GET /api/todos?status=done should filter correctly."""
        client.post('/api/todos', json={"title": "Done task", "status": "done"})
        client.post('/api/todos', json={"title": "Pending task", "status": "pending"})

        r = client.get('/api/todos?status=done')
        todos = r.get_json()
        assert len(todos) >= 1
        assert all(t['status'] == 'done' for t in todos)

    def test_filter_by_priority(self, client):
        """GET /api/todos?priority=high should filter correctly."""
        client.post('/api/todos', json={"title": "High task", "priority": "high"})
        client.post('/api/todos', json={"title": "Low task", "priority": "low"})

        r = client.get('/api/todos?priority=high')
        todos = r.get_json()
        assert len(todos) >= 1
        assert all(t['priority'] == 'high' for t in todos)


class TestCategoryRelationship:
    """FAIL until TODO 5 is done — foreign key + relationship."""

    def test_category_model_exists(self, client):
        """CategoryModel should be importable (uncommented)."""
        try:
            from app import CategoryModel
            assert CategoryModel is not None
        except ImportError:
            assert False, "Cannot import 'CategoryModel' — did you uncomment it?"

    def test_create_category(self, client):
        """POST /api/categories should create a category."""
        r = client.post('/api/categories', json={"name": "Work"})
        assert r.status_code == 201
        assert r.get_json()['name'] == "Work"

    def test_get_categories(self, client):
        """GET /api/categories should return all categories."""
        client.post('/api/categories', json={"name": "Work"})
        client.post('/api/categories', json={"name": "Personal"})
        r = client.get('/api/categories')
        assert r.status_code == 200
        assert len(r.get_json()) == 2

    def test_todo_has_category_id(self, client):
        """TodoModel should have a 'category_id' column."""
        from app import TodoModel
        cols = [c.name for c in TodoModel.__table__.columns]
        assert 'category_id' in cols, "TodoModel missing 'category_id' column — complete TODO 5"

    def test_create_todo_with_category(self, client):
        """Create a category, then create a todo assigned to it."""
        r = client.post('/api/categories', json={"name": "Work"})
        cat_id = r.get_json()['id']

        r = client.post('/api/todos', json={
            "title": "Finish report",
            "category_id": cat_id
        })
        assert r.status_code == 201
        data = r.get_json()
        assert data['category_id'] == cat_id

    def test_todo_without_category(self, client):
        """A todo without a category should have category_id = null."""
        r = client.post('/api/todos', json={"title": "No category"})
        assert r.status_code == 201
        assert r.get_json()['category_id'] is None

    def test_category_todo_count(self, client):
        """Category to_dict() should include the count of its todos."""
        r = client.post('/api/categories', json={"name": "Work"})
        cat_id = r.get_json()['id']

        client.post('/api/todos', json={"title": "Task 1", "category_id": cat_id})
        client.post('/api/todos', json={"title": "Task 2", "category_id": cat_id})

        r = client.get(f'/api/categories/{cat_id}')
        assert r.status_code == 200
        assert r.get_json()['todo_count'] == 2

    def test_filter_by_category(self, client):
        """GET /api/todos?category_id=1 should filter by category."""
        r = client.post('/api/categories', json={"name": "Work"})
        cat_id = r.get_json()['id']

        client.post('/api/todos', json={"title": "Work task", "category_id": cat_id})
        client.post('/api/todos', json={"title": "No category task"})

        r = client.get(f'/api/todos?category_id={cat_id}')
        todos = r.get_json()
        assert len(todos) == 1
        assert todos[0]['title'] == "Work task"
