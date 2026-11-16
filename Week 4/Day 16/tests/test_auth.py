import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.storage import users
import app.storage as storage


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_users():
    users.clear()
    storage.next_user_id = 1


def test_register_user():

    response = client.post(
        "/auth/register",
        json={
            "username": "john",
            "email": "john@example.com",
            "password": "SecurePass123"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == "john"
    assert "password" not in data
    assert "hashed_password" not in data


def test_duplicate_email():

    user = {
        "username": "john",
        "email": "john@example.com",
        "password": "SecurePass123"
    }

    client.post("/auth/register", json=user)

    response = client.post(
        "/auth/register",
        json=user
    )

    assert response.status_code == 409


def test_missing_credentials():

    response = client.post(
        "/auth/login",
        json={
            "email": "john@example.com"
        }
    )

    assert response.status_code == 422


def test_unknown_account():

    response = client.post(
        "/auth/login",
        json={
            "email": "unknown@example.com",
            "password": "SecurePass123"
        }
    )

    assert response.status_code == 401


def test_successful_login():

    client.post(
        "/auth/register",
        json={
            "username": "john",
            "email": "john@example.com",
            "password": "SecurePass123"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "john@example.com",
            "password": "SecurePass123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_current_user():

    client.post(
        "/auth/register",
        json={
            "username": "john",
            "email": "john@example.com",
            "password": "SecurePass123"
        }
    )

    login = client.post(
        "/auth/login",
        json={
            "email": "john@example.com",
            "password": "SecurePass123"
        }
    )

    token = login.json()["access_token"]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json()["email"] == "john@example.com"


def test_missing_token():

    response = client.get("/auth/me")

    assert response.status_code == 401


def test_invalid_token():

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    )

    assert response.status_code == 401