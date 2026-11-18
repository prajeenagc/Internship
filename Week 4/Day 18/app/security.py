
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from app.config import settings


password_hash = PasswordHash.recommended()


# Password hashing
def hash_password(password: str) -> str:
    return password_hash.hash(password)


# Password verification
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(plain_password, hashed_password)


# JWT creation
def create_access_token(user_id: int) -> str:

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token


# JWT verification
def verify_access_token(token: str) -> dict:

    payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )

    return payload
