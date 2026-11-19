import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db
from app.models import User, Task


# Sets up a separate SQLite database for testing.
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

# Creates database sessions for the tests.
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Prepares the test database, users, task, and API client.
@pytest.fixture
def setup():
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    alice = User(username="alice", role="user")
    bob = User(username="bob", role="admin")

    db.add_all([alice, bob])
    db.commit()

    db.refresh(alice)
    db.refresh(bob)

    task = Task(
        title="Alice private task",
        owner_id=alice.id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    # Replaces the application's database dependency with the test database.
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)

    yield client, db, alice, bob, task

    # Cleans up after each test.
    app.dependency_overrides.clear()
    db.close()
    Base.metadata.drop_all(bind=engine)


# Checks that one user cannot read another user's task.
def test_cross_user_read(setup):
    client, db, alice, bob, task = setup

    response = client.get(
        f"/tasks/{task.id}",
        headers={"X-User-ID": str(bob.id)}
    )

    assert response.status_code == 404


# Checks that one user cannot update another user's task.
def test_cross_user_update(setup):
    client, db, alice, bob, task = setup

    response = client.put(
        f"/tasks/{task.id}",
        headers={"X-User-ID": str(bob.id)},
        json={"title": "Unauthorized change"}
    )

    assert response.status_code == 404

    db.refresh(task)
    assert task.title == "Alice private task"


# Checks that one user cannot delete another user's task.
def test_cross_user_delete(setup):
    client, db, alice, bob, task = setup

    response = client.delete(
        f"/tasks/{task.id}",
        headers={"X-User-ID": str(bob.id)}
    )

    assert response.status_code == 404

    existing_task = db.query(Task).filter(
        Task.id == task.id
    ).first()

    assert existing_task is not None


# Checks that regular users cannot access admin-only actions.
def test_regular_user_cannot_delete_user(setup):
    client, db, alice, bob, task = setup

    response = client.delete(
        f"/admin/users/{bob.id}",
        headers={"X-User-ID": str(alice.id)}
    )

    assert response.status_code == 403


# Checks that administrators can delete other users.
def test_admin_can_access_admin_action(setup):
    client, db, alice, bob, task = setup

    # Creates a user without tasks to test deletion.
    target = User(username="charlie", role="user")
    db.add(target)
    db.commit()
    db.refresh(target)

    response = client.delete(
        f"/admin/users/{target.id}",
        headers={"X-User-ID": str(bob.id)}
    )

    assert response.status_code == 200

    deleted_user = db.query(User).filter(
        User.id == target.id
    ).first()

    assert deleted_user is None