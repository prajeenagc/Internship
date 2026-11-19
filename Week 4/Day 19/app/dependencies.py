from fastapi import Depends, HTTPException,Header
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User


#funstion to identify currently logged-in user
def get_current_user(
    current_user_id: int = Header(..., alias="X-User-ID"),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == current_user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not authenticated"
        )

    return user


#function that restricts access to administrators
def require_admin(
        current_user:User=Depends(get_current_user)
):
    if current_user.role !="admin":
        raise HTTPException(
            status_code=403,
            detail="Administrator access required"
        )

    return current_user