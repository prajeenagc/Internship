from datetime import datetime, timedelta, timezone

import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from app.storage import users
from app.schemas import UserCreate, UserLogin


SECRET_KEY = "day16-development-secret-change-this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# Hash password
def hash_password(password: str):
    return password_hash.hash(password)


# Verify password
def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)


# Register user
def register_user(user_data: UserCreate):

    for user in users:
        if user["email"].lower() == user_data.email.lower():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

    from app.storage import next_user_id
    import app.storage as storage

    new_user = {
        "id": storage.next_user_id,
        "username": user_data.username,
        "email": user_data.email,
        "hashed_password": hash_password(user_data.password),
        "is_active": True
    }

    users.append(new_user)
    storage.next_user_id += 1

    return new_user


# Authenticate user
def authenticate_user(user_data: UserLogin):

    for user in users:
        if user["email"].lower() == user_data.email.lower():

            if not verify_password(
                user_data.password,
                user["hashed_password"]
            ):
                return None

            return user

    return None


# Create access token
def create_access_token(user_id: int):

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# Get current user
def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    current_user = None

    for user in users:
        if str(user["id"]) == user_id:
            current_user = user
            break

    if current_user is None or not current_user["is_active"]:
        raise credentials_exception

    return current_user