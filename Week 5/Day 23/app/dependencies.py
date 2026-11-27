from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_current_user(
    user_id: int | None = Header(
        default=None,
        alias="X-User-ID"
    ),
    db: Session = Depends(get_db)
):

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user