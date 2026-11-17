from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserCreate
from app.security import hash_password


def register_user(user_data: UserCreate, db: Session):

    username = user_data.username.strip()
    email = str(user_data.email).strip().lower()

    # Check if username already exists
    existing_username = db.query(User).filter(
        User.username == username
    ).first()

    if existing_username:
        raise ValueError("Username already exists")

    # Check if email already exists
    existing_email = db.query(User).filter(
        User.email == email
    ).first()

    if existing_email:
        raise ValueError("Email already registered")

    # Hash password
    hashed_password = hash_password(user_data.password)

    # Create user
    new_user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user