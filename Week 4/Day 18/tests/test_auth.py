
import jwt
import pytest

from datetime import datetime, timedelta, timezone
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.models import User
from app.config import settings
from app.security import hash_password


# Separate PostgreSQL test database
test_engine = create_engine(settings.TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)


# Override the application database dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():

    Base.metadata.create_all(bind=test_engine)

    db = TestingSessionLocal()

    user = User(
        username="testuser",
        email="test@example.com",
        hashed_password=hash_password("password123")
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    user_id = user.id

    db.close()

    with TestClient(app) as test_client:
        yield test_client, user_id

    Base.metadata.drop_all(bind=test_engine)


# 1. Invalid password
def test_invalid_password(client):

    test_client, user_id = client

    response = test_client.post(
        "/login",
        json={
            "email": "test@example.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401


# 2. Missing token
def test_missing_token(client):

    test_client, user_id = client

    response = test_client.get("/me")

    assert response.status_code == 401


# 3. Tampered token
def test_tampered_token(client):

    test_client, user_id = client

    login_response = test_client.post(
        "/login",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    token = login_response.json()["access_token"]

    tampered_token = token + "tampered"

    response = test_client.get(
        "/me",
        headers={
            "Authorization": f"Bearer {tampered_token}"
        }
    )

    assert response.status_code == 401


# 4. Expired token
def test_expired_token(client):

    test_client, user_id = client

    expired_payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc) - timedelta(minutes=5)
    }

    expired_token = jwt.encode(
        expired_payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    response = test_client.get(
        "/me",
        headers={
            "Authorization": f"Bearer {expired_token}"
        }
    )

    assert response.status_code == 401


# 5. Successful login and current-user lookup
def test_successful_login(client):

    test_client, user_id = client

    login_response = test_client.post(
        "/login",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    # Verify JWT payload
    payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )

    assert payload["sub"] == str(user_id)
    assert "exp" in payload
    assert "password" not in payload
    assert "hashed_password" not in payload

    # Verify current-user lookup
    me_response = test_client.get(
        "/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert me_response.status_code == 200
    assert me_response.json()["email"] == "test@example.com"
