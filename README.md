# Lab 3: Validation

## Overview

In the previous class activity, you implemented basic schema validation: required fields, type checking, and numeric ranges.

Real APIs need more than that. In this lab you will implement four validation rules that go beyond basic schema checks:

| Validation Type | What It Checks | Where to Implement |
|---|---|---|
| **Business rule** | Does the referenced store actually exist? | `app.py` (route handler) |
| **Cross-field** | Is discount_price ≤ price? | `schemas.py` (schema hook) |
| **Input sanitization** | Trim whitespace, reject blank names | `schemas.py` (schema hook) |
| **Data integrity** | No duplicate item names in the same store | `app.py` (route handler) |

Notice that some validation belongs in the **schema** (data shape, field relationships) and some belongs in the **route handler** (application state, data already in memory). This separation matters in real codebases.

---

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Running Tests

You do **not** need the server running to run tests.

```bash
pytest tests/ -v
```

Before you implement anything, you should see:

- `TestBasicValidation` → all PASS (provided for you)
- `TestStoreExists` → FAIL
- `TestDiscountPrice` → FAIL
- `TestNameTrimming` → FAIL
- `TestDuplicateNames` → FAIL

After you complete all TODOs, all tests should PASS.

---

## Swagger UI

If you want to test manually in addition to pytest:

```bash
python app.py
```

Then open http://127.0.0.1:5000/swagger-ui

---

## Pre-Populated Data

The API starts with two stores (no items):

| Store ID | Name |
|---|---|
| 1 | Tech Store |
| 2 | Furniture Store |

---

## Your Tasks

### TODO 1 — Business Validation (app.py)

**store_id must refer to an existing store.**

This can't be done in the schema because the schema doesn't know what stores exist. It must be checked in the route handler.

```
POST /items
{"name": "Ghost Item", "price": 5.00, "store_id": 999}
→ 404: "Store not found."
```

Hint: use the `store_exists()` helper and `abort()`.

---

### TODO 2 — Cross-Field Validation (schemas.py)

**If discount_price is provided, it must be ≤ price.**

This belongs in the schema because it's a relationship between two fields in the same request. Use `@validates_schema` — it gives you access to all fields at once.

```
POST /items
{"name": "Bad Deal", "price": 50, "discount_price": 100, "store_id": 1}
→ 422: "Discount price cannot exceed regular price."
```

Note: if discount_price is `null` or not provided, skip this check.

---

### TODO 3 — Input Sanitization (schemas.py)

**Strip whitespace from name, reject blank names after stripping.**

This belongs in the schema because it's about cleaning up input data before it reaches your route handler. Use `@pre_load` to trim, and `@validates("name")` to reject blanks.

```
POST /items
{"name": "   ", "price": 5, "store_id": 1}
→ 422: "Name cannot be blank."

POST /items
{"name": "  Keyboard  ", "price": 75, "store_id": 1}
→ 201: name is saved as "Keyboard" (trimmed)
```

Important: both `@pre_load` and `@validates` methods need `**kwargs` in their signature.

---

### TODO 4 — Data Integrity (app.py)

**No duplicate item names within the same store (case-insensitive).**

This can't be done in the schema because the schema doesn't know what items already exist. It must be checked in the route handler.

The same name in a *different* store is fine.

```
# First request succeeds
POST /items  {"name": "Laptop", "price": 1000, "store_id": 1}  → 201

# Same name, same store → rejected
POST /items  {"name": "Laptop", "price": 800, "store_id": 1}  → 409

# Same name, different store → accepted
POST /items  {"name": "Laptop", "price": 1200, "store_id": 2}  → 201
```

Hint: use the `duplicate_name_in_store()` helper and `abort()`.

---

## File Guide

| File | What to Do |
|---|---|
| `schemas.py` | Implement TODO 2 and TODO 3 |
| `app.py` | Implement TODO 1 and TODO 4 |
| `tests/test_validation.py` | Read to understand expected behavior (do not modify) |
| `tests/conftest.py` | Test setup (do not modify) |
---

## Submission

1. Complete all four TODOs
2. Run `pytest tests/ -v` and verify all tests pass
3. Push to your GitHub Classroom repository
4. Submit the repo link on bCourses
