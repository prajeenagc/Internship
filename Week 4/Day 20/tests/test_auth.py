# Check that a new user can register successfully.
def test_register_user(client):

    response = client.post(
        "/register",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 201

    assert response.json()["username"] == "alice"

    # Make sure the hashed password is never included in the response.
    assert "hashed_password" not in response.json()


# Check that registering with an email that already exists is rejected.
def test_duplicate_registration(client):

    user_data = {
        "username": "alice",
        "email": "alice@example.com",
        "password": "password123"
    }

    client.post("/register", json=user_data)

    response = client.post(
        "/register",
        json=user_data
    )

    assert response.status_code == 409


# Check that a user can log in with the correct credentials.
def test_successful_login(client):

    # Create an account first so the user has something to log in with.
    client.post(
        "/register",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": "alice@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    assert "access_token" in response.json()

    assert response.json()["token_type"] == "bearer"


# Check that login fails when the password is incorrect.
def test_wrong_password(client):

    client.post(
        "/register",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": "alice@example.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401


# Private routes should not be accessible without an access token.
def test_private_route_without_token(client):

    response = client.get("/users/me")

    assert response.status_code == 401


# Check that an invalid token cannot be used to access a private route.
def test_private_route_with_invalid_token(client):

    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer invalid_token"
        }
    )

    assert response.status_code == 401


# Check that an authenticated user can access their own profile.
def test_authenticated_user_can_access_profile(client):

    client.post(
        "/register",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "email": "alice@example.com",
            "password": "password123"
        }
    )

    # Extract the access token returned after successful login.
    token = login_response.json()["access_token"]

    response = client.get(
        "/users/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    assert response.json()["username"] == "alice"