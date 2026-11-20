import jwt

from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash

from app.config import settings


# Use the recommended password hashing algorithm and settings.
password_hash = PasswordHash.recommended()


# Hash the password before storing it in the database.
def hash_password(password: str):

    return password_hash.hash(password)


# Compare the entered password with the stored password hash.
def verify_password(
    plain_password: str,
    hashed_password: str
):

    return password_hash.verify(
        plain_password,
        hashed_password
    )


# Generate a JWT access token for the authenticated user.
def create_access_token(user_id: int):

    # Set the token expiration time using the configured duration.
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Store the user's ID and token expiration time in the payload.
    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    # Sign the token using the application secret key.
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token