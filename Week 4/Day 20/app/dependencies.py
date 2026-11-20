import jwt

from jwt.exceptions import InvalidTokenError

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.config import settings


# Extract the bearer token from the Authorization header.
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


# Get the currently authenticated user from the access token.
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    # Return the same authentication error for invalid credentials.
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:

        # Decode the token and verify its signature and expiration.
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        # Get the user ID stored in the token.
        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        user_id = int(user_id)

    except (InvalidTokenError, ValueError, TypeError):
        raise credentials_exception

    # Find the user associated with the token.
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    # Reject the request if the user doesn't exist or is inactive.
    if user is None or not user.is_active:
        raise credentials_exception

    return user