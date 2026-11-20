# Register a user and log in to get their access token.
def register_and_login(client, username, email):

    client.post(
        "/register",
        json={
            "username": username,
            "email": email,
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": email,
            "password": "password123"
        }
    )

    return response.json()["access_token"]


# Make sure users cannot access items that belong to someone else.
def test_two_users_cannot_access_each_others_items(client):

    # Create Alice and Bob and get their access tokens.
    alice_token = register_and_login(
        client,
        "alice",
        "alice@example.com"
    )

    bob_token = register_and_login(
        client,
        "bob",
        "bob@example.com"
    )

    # Each user needs their own token to access protected routes.
    alice_headers = {
        "Authorization": f"Bearer {alice_token}"
    }

    bob_headers = {
        "Authorization": f"Bearer {bob_token}"
    }

    # Alice creates an item that belongs to her account.
    alice_item = client.post(
        "/items",
        json={
            "title": "Alice private item"
        },
        headers=alice_headers
    )

    assert alice_item.status_code == 201

    item_id = alice_item.json()["id"]

    # Bob should only see his own items, not Alice's.
    bob_items = client.get(
        "/items",
        headers=bob_headers
    )

    assert bob_items.status_code == 200
    assert bob_items.json() == []

    # Bob should not be able to retrieve Alice's item by its ID.
    bob_retrieve = client.get(
        f"/items/{item_id}",
        headers=bob_headers
    )

    assert bob_retrieve.status_code == 404

    # Bob should not be able to modify an item he doesn't own.
    bob_update = client.put(
        f"/items/{item_id}",
        json={
            "title": "Hacked item"
        },
        headers=bob_headers
    )

    assert bob_update.status_code == 404

    # Bob should not be able to delete Alice's item either.
    bob_delete = client.delete(
        f"/items/{item_id}",
        headers=bob_headers
    )

    assert bob_delete.status_code == 404

    # Make sure Alice still has access to her item.
    alice_retrieve = client.get(
        f"/items/{item_id}",
        headers=alice_headers
    )

    assert alice_retrieve.status_code == 200

    assert alice_retrieve.json()["title"] == "Alice private item"