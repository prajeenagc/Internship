from jose import jwt

from app.database import SessionLocal
from app.models import User, Task
from app.config import settings


db = SessionLocal()

try:
    # Create a test user.
    user = User(username="testuser")
    db.add(user)
    db.flush()

    # Create two tasks belonging to this user.
    task1 = Task(title="Learn GraphQL", owner_id=user.id)
    task2 = Task(title="Practice Ariadne", owner_id=user.id)

    db.add_all([task1, task2])
    db.commit()

    # Generate a JWT for the test user.
    token = jwt.encode(
        {"sub": str(user.id)},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    print("Test user created!")
    print("User ID:", user.id)
    print("JWT:", token)

finally:
    db.close()