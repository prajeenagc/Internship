from fastapi import FastAPI, HTTPException, status, Depends

from app.schemas import (
    UserCreate,
    UserLogin,
    UserResponse,
    TokenResponse
)

from app.auth import (
    register_user,
    authenticate_user,
    create_access_token,
    get_current_user
)


app = FastAPI(title="Day 16 Authentication API")


# Registration
@app.post(
    "/auth/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(user_data: UserCreate):

    new_user = register_user(user_data)

    return new_user


# Login
@app.post(
    "/auth/login",
    response_model=TokenResponse
)
def login(user_data: UserLogin):

    user = authenticate_user(user_data)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(user["id"])

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# Current user
@app.get(
    "/auth/me",
    response_model=UserResponse
)
def get_me(current_user: dict = Depends(get_current_user)):

    return current_user