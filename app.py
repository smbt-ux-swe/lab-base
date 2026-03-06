"""
app.py — Flask REST API for Stores and Items

ALREADY PROVIDED:
  - App setup, blueprints, in-memory storage
  - GET and POST routes that work
  - Helper functions for validation

YOUR TASKS (TODO 1 and TODO 4):
  Look for TODO comments in the post() method below.
  These validations belong in the route handler because
  they depend on application state (the data in memory),
  not just the shape of the request.

WHY SOME VALIDATION IS HERE vs IN SCHEMAS:
  - schemas.py handles data shape: types, ranges, field relationships
  - app.py handles application logic: "does this store exist?", "is this name taken?"
  This is how real APIs separate concerns.
"""

from flask import Flask
from flask_smorest import Api, Blueprint, abort
from flask.views import MethodView
from schemas import ItemSchema, ItemCreateSchema, StoreSchema

app = Flask(__name__)

app.config["API_TITLE"] = "Advanced Validation API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)


# ============================================================
# In-Memory Storage
# ============================================================

stores = [
    {"id": 1, "name": "Tech Store"},
    {"id": 2, "name": "Furniture Store"},
]

items = []

next_item_id = 1


# ============================================================
# Helper Functions (use these in your TODOs)
# ============================================================

def store_exists(store_id):
    """Return True if a store with this ID exists."""
    return any(s["id"] == store_id for s in stores)


def duplicate_name_in_store(name, store_id):
    """Return True if an item with this name already exists in the store.
    Comparison is case-insensitive.
    """
    return any(
        i["store_id"] == store_id and i["name"].lower() == name.lower()
        for i in items
    )


# ============================================================
# Item Routes
# ============================================================

items_blp = Blueprint("items", __name__, description="Operations on items")


@items_blp.route("/items")
class ItemList(MethodView):

    @items_blp.response(200, ItemSchema(many=True))
    def get(self):
        """List all items."""
        return items

    @items_blp.arguments(ItemCreateSchema)
    @items_blp.response(201, ItemSchema)
    def post(self, item_data):
        """Create a new item.

        When this code runs, Marshmallow has already validated:
          - name exists and is 1-100 chars
          - price exists and is >= 0
          - store_id exists and is an integer

        If you completed TODO 2 and 3 in schemas.py:
          - name has been trimmed and blank names rejected
          - discount_price has been checked against price

        YOUR JOB HERE: Add route-level validation that depends
        on the current application state.
        """
        global next_item_id

        # --------------------------------------------------
        # TODO 1: Business Validation — Store must exist
        #
        #   Check if item_data["store_id"] refers to a real
        #   store. If not, reject the request.
        #
        #   Use: store_exists() helper function
        #   Use: abort(404, message="Store not found.")
        #
        #   Test: {"name": "Ghost", "price": 5, "store_id": 999}
        #         should return 404
        # --------------------------------------------------

        # --------------------------------------------------
        # TODO 4: Data Integrity — No duplicate names per store
        #
        #   Two items in the SAME store cannot have the same
        #   name (case-insensitive). Same name in a DIFFERENT
        #   store is fine.
        #
        #   Use: duplicate_name_in_store() helper function
        #   Use: abort(409, message="An item with this name already exists in this store.")
        #
        #   Test: Create "Laptop" in store 1, then try to
        #         create "Laptop" in store 1 again → 409
        #   Test: Create "Laptop" in store 1, then
        #         create "Laptop" in store 2 → 201 (OK)
        # --------------------------------------------------

        new_item = {
            "id": next_item_id,
            "name": item_data["name"],
            "price": item_data["price"],
            "discount_price": item_data.get("discount_price"),
            "store_id": item_data["store_id"],
        }
        items.append(new_item)
        next_item_id += 1

        return new_item


# ============================================================
# Store Routes
# ============================================================

stores_blp = Blueprint("stores", __name__, description="Operations on stores")


@stores_blp.route("/stores")
class StoreList(MethodView):

    @stores_blp.response(200, StoreSchema(many=True))
    def get(self):
        """List all stores."""
        return stores


# ============================================================
# Register Blueprints
# ============================================================

api.register_blueprint(items_blp)
api.register_blueprint(stores_blp)

if __name__ == "__main__":
    app.run(debug=True)
