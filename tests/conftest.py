"""Test configuration — do not modify."""

import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    """Create a test client with a fresh database."""
    app.config['TESTING'] = True

    try:
        from app import db
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()
            with app.test_client() as client:
                yield client
            db.drop_all()
    except ImportError:
        with app.test_client() as client:
            yield client
