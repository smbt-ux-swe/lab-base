import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
from app import app, items, stores


@pytest.fixture()
def client():
    """Create a test client. Resets item data before each test."""
    app.config["TESTING"] = True

    # Reset items before each test (stores stay the same)
    items.clear()

    with app.test_client() as client:
        yield client
