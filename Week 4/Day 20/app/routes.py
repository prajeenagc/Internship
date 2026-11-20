from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User

from app.schemas import (
    UserCreate,
    UserLogin,
    UserResponse,
    TokenResponse,
    ItemCreate,
    ItemUpdate,
    ItemResponse
)

from app.security import create_access_token
from app.dependencies import get_current_user

from app.services import (
    register_user,
    authenticate_user,
    create_item,
    get_user_items,
    get_item,
    update_item,
    delete_item
)


router = APIRouter()


# REGISTRATION

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    # Pass the registration data to the service function.
    return register_user(
        user_data,
        db
    )


# LOGIN

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    # Verify the user's login credentials.
    user = authenticate_user(
        user_data.email,
        user_data.password,
        db
    )

    # Generate an access token for the authenticated user.
    token = create_access_token(user.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# PRIVATE PROFILE

@router.get(
    "/users/me",
    response_model=UserResponse
)
def get_profile(
    current_user: User = Depends(get_current_user)
):

    # Return the profile of the currently logged-in user.
    return current_user


# CREATE ITEM

@router.post(
    "/items",
    response_model=ItemResponse,
    status_code=201
)
def add_item(
    item_data: ItemCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return create_item(
        item_data,
        current_user,
        db
    )


# GET ALL CURRENT USER ITEMS

@router.get(
    "/items",
    response_model=list[ItemResponse]
)
def list_items(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # Return only the items belonging to the logged-in user.
    return get_user_items(
        current_user,
        db
    )


# GET SINGLE ITEM

@router.get(
    "/items/{item_id}",
    response_model=ItemResponse
)
def retrieve_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_item(
        item_id,
        current_user,
        db
    )


# UPDATE ITEM

@router.put(
    "/items/{item_id}",
    response_model=ItemResponse
)
def edit_item(
    item_id: int,
    item_data: ItemUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return update_item(
        item_id,
        item_data,
        current_user,
        db
    )


# DELETE ITEM

@router.delete("/items/{item_id}")
def remove_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return delete_item(
        item_id,
        current_user,
        db
    )