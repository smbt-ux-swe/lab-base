"""
schemas.py — Marshmallow Schemas

ALREADY PROVIDED:
  - Required fields, types, length limits, numeric ranges
  - These use standard Marshmallow features from previous labs

YOUR TASKS (TODO 2 and TODO 3):
  Look for TODO comments below. You will add validation hooks
  that go beyond basic field-level checks.

USEFUL IMPORTS (already included for you):
  - validates_schema: access ALL fields at once during validation
  - pre_load: modify data BEFORE validation runs
  - validates: validate a single field after type checking
  - ValidationError: raise this to reject invalid data
"""

from marshmallow import (
    Schema,
    fields,
    validate,
    validates,
    validates_schema,
    pre_load,
    ValidationError,
)


class StoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class ItemSchema(Schema):
    """Used for responses. All fields included."""

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    discount_price = fields.Float(allow_none=True)
    store_id = fields.Int(required=True)


class ItemCreateSchema(Schema):
    """Used for creating items. Basic validation is done for you.

    Basic validation already handles:
      - name is required, max 100 characters
      - price is required, must be >= 0
      - discount_price is optional (can be null)
      - store_id is required
    """

    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    price = fields.Float(required=True, validate=validate.Range(min=0))
    discount_price = fields.Float(load_default=None, allow_none=True)
    store_id = fields.Int(required=True)

    # ----------------------------------------------------------
    # TODO 3: Security Validation — Trim whitespace, reject blanks
    #
    #   Step A: Add a @pre_load method that strips leading/trailing
    #           whitespace from "name" BEFORE validation runs.
    #
    #   Step B: Add a @validates("name") method that rejects
    #           names that are empty after stripping.
    #
    #   Important: Both methods need **kwargs in the signature.
    #
    #   Template:
    #
    #       @pre_load
    #       def strip_name(self, data, **kwargs):
    #           # modify data["name"] here
    #           return data  # must return data!
    #
    #       @validates("name")
    #       def reject_blank_name(self, value, **kwargs):
    #           # check value here
    #           # raise ValidationError("Name cannot be blank.")
    #           pass
    #
    #   Test: {"name": "   ", "price": 5, "store_id": 1}
    #         should fail with 422
    #
    #   Test: {"name": "  Laptop  ", ...}
    #         should succeed with name trimmed to "Laptop"
    # ----------------------------------------------------------

    # ----------------------------------------------------------
    # TODO 2: Cross-Field Validation — discount_price <= price
    #
    #   If discount_price is provided (not None), it must be
    #   less than or equal to price.
    #
    #   Use @validates_schema because you need access to BOTH
    #   fields at once. A single-field @validates only sees
    #   one value.
    #
    #   Template:
    #
    #       @validates_schema
    #       def check_discount(self, data, **kwargs):
    #           discount = data.get("discount_price")
    #           price = data.get("price")
    #           # compare them here
    #           # raise ValidationError("Discount price cannot exceed regular price.")
    #
    #   Test: {"name": "Mouse", "price": 50, "discount_price": 100, "store_id": 1}
    #         should fail with 422
    # ----------------------------------------------------------
