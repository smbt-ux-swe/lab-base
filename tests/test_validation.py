"""
test_validation.py — Tests for Advanced Validation Lab

Run with: pytest tests/ -v

These tests use Flask's test client, so you do NOT need
the server running. Just run pytest directly.

BEFORE you implement the TODOs:
  - Tests in "Basic validation" section should PASS (already provided)
  - Tests in "TODO" sections will FAIL (that's expected!)

AFTER you implement all TODOs:
  - ALL tests should PASS
"""


# ==============================================================
# Basic Validation (already provided — should pass from the start)
# ==============================================================

class TestBasicValidation:
    """These test the validation that's already in the starter code."""

    def test_valid_item_returns_201(self, client):
        response = client.post("/items", json={
            "name": "Laptop",
            "price": 1000,
            "discount_price": 900,
            "store_id": 1,
        })
        assert response.status_code == 201

    def test_missing_name_returns_422(self, client):
        response = client.post("/items", json={
            "price": 100,
            "store_id": 1,
        })
        assert response.status_code == 422

    def test_negative_price_returns_422(self, client):
        response = client.post("/items", json={
            "name": "Free Lunch",
            "price": -5,
            "store_id": 1,
        })
        assert response.status_code == 422

    def test_missing_store_id_returns_422(self, client):
        response = client.post("/items", json={
            "name": "Orphan Item",
            "price": 10,
        })
        assert response.status_code == 422

    def test_get_items_returns_200(self, client):
        response = client.get("/items")
        assert response.status_code == 200

    def test_get_stores_returns_200(self, client):
        response = client.get("/stores")
        assert response.status_code == 200


# ==============================================================
# TODO 1: Business Validation — store_id must exist
# ==============================================================

class TestStoreExists:
    """These tests will FAIL until you implement TODO 1 in app.py."""

    def test_nonexistent_store_is_rejected(self, client):
        response = client.post("/items", json={
            "name": "Ghost Item",
            "price": 5.00,
            "store_id": 999,
        })
        assert response.status_code == 404

    def test_existing_store_is_accepted(self, client):
        response = client.post("/items", json={
            "name": "Real Item",
            "price": 25.00,
            "store_id": 1,
        })
        assert response.status_code == 201


# ==============================================================
# TODO 2: Cross-Field Validation — discount_price <= price
# ==============================================================

class TestDiscountPrice:
    """These tests will FAIL until you implement TODO 2 in schemas.py."""

    def test_discount_higher_than_price_is_rejected(self, client):
        response = client.post("/items", json={
            "name": "Bad Deal",
            "price": 50.00,
            "discount_price": 100.00,
            "store_id": 1,
        })
        assert response.status_code == 422

    def test_discount_equal_to_price_is_accepted(self, client):
        response = client.post("/items", json={
            "name": "No Discount",
            "price": 50.00,
            "discount_price": 50.00,
            "store_id": 1,
        })
        assert response.status_code == 201

    def test_discount_lower_than_price_is_accepted(self, client):
        response = client.post("/items", json={
            "name": "Good Deal",
            "price": 100.00,
            "discount_price": 79.99,
            "store_id": 1,
        })
        assert response.status_code == 201

    def test_null_discount_is_accepted(self, client):
        response = client.post("/items", json={
            "name": "No Sale",
            "price": 30.00,
            "discount_price": None,
            "store_id": 1,
        })
        assert response.status_code == 201

    def test_missing_discount_is_accepted(self, client):
        response = client.post("/items", json={
            "name": "Simple Item",
            "price": 20.00,
            "store_id": 1,
        })
        assert response.status_code == 201


# ==============================================================
# TODO 3: Security Validation — trim whitespace, reject blanks
# ==============================================================

class TestNameTrimming:
    """These tests will FAIL until you implement TODO 3 in schemas.py."""

    def test_whitespace_only_name_is_rejected(self, client):
        response = client.post("/items", json={
            "name": "   ",
            "price": 20.00,
            "store_id": 1,
        })
        assert response.status_code == 422

    def test_name_with_spaces_is_trimmed(self, client):
        response = client.post("/items", json={
            "name": "  Keyboard  ",
            "price": 75.00,
            "store_id": 1,
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["name"] == "Keyboard"


# ==============================================================
# TODO 4: Data Integrity — no duplicate names per store
# ==============================================================

class TestDuplicateNames:
    """These tests will FAIL until you implement TODO 4 in app.py."""

    def test_duplicate_name_in_same_store_is_rejected(self, client):
        # Create first item
        client.post("/items", json={
            "name": "Laptop",
            "price": 1000,
            "store_id": 1,
        })
        # Try to create same name in same store
        response = client.post("/items", json={
            "name": "Laptop",
            "price": 800,
            "store_id": 1,
        })
        assert response.status_code == 409

    def test_duplicate_name_is_case_insensitive(self, client):
        client.post("/items", json={
            "name": "Laptop",
            "price": 1000,
            "store_id": 1,
        })
        response = client.post("/items", json={
            "name": "laptop",
            "price": 500,
            "store_id": 1,
        })
        assert response.status_code == 409

    def test_same_name_in_different_store_is_accepted(self, client):
        client.post("/items", json={
            "name": "Laptop",
            "price": 1000,
            "store_id": 1,
        })
        response = client.post("/items", json={
            "name": "Laptop",
            "price": 1200,
            "store_id": 2,
        })
        assert response.status_code == 201
