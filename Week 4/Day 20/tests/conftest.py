import os

# Provide a test secret key if one hasn't already been set.
os.environ.setdefault(
    "SECRET_KEY",
    "test_secret_key_for_testing_only"
)

import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db


# Use an in-memory SQLite database for testing instead of the actual database.
engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)


# Create a separate session factory for test database operations.
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Override the database dependency so API requests use the test database.
def override_get_db():

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


# Tell FastAPI to use our test database whenever get_db is requested.
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():

    # Create all database tables before running the tests.
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as test_client:
        yield test_client

    # Remove the tables after the tests are finished.
    Base.metadata.drop_all(bind=engine)