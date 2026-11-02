from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test 1: Create task
def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn FastAPI",
            "description": "Practice automated testing"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn FastAPI"
    assert response.json()["description"] == "Practice automated testing"
    assert response.json()["is_done"] is False
    assert "id" in response.json()


# Test 2: Get an existing task
def test_get_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Read task",
            "description": "Test task retrieval"
        }
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Read task"


# Test 3: Update a task
def test_update_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Old title",
            "description": "Old description"
        }
    )

    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated title",
            "description": "Updated description",
            "is_done": True
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"
    assert response.json()["description"] == "Updated description"
    assert response.json()["is_done"] is True


# Test 4: Delete a task
def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Delete me",
            "description": "This task will be deleted"
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Task not found"


# Test 5: Get a nonexistent task
def test_get_nonexistent_task():
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


# Test 6: Create task with invalid title
def test_create_task_with_empty_title():
    response = client.post(
        "/tasks",
        json={
            "title": "",
            "description": "Invalid task"
        }
    )

    assert response.status_code == 422
