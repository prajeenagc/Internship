import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User, Item
from app.schemas import UserCreate, ItemCreate, ItemUpdate

from app.security import hash_password, verify_password


logger = logging.getLogger(__name__)


# USER REGISTRATION

def register_user(
    user_data: UserCreate,
    db: Session
):

    # Check whether the email or username is already in use.
    existing_user = db.query(User).filter(
        (User.email == user_data.email) |
        (User.username == user_data.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Username or email already registered"
        )

    # Hash the password before saving the new user.
    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )

    try:

        db.add(user)
        db.commit()
        db.refresh(user)

    except Exception:
        # Undo the database changes if registration fails.
        db.rollback()
        raise

    logger.info("User registered: id=%s", user.id)

    return user


# USER LOGIN

def authenticate_user(
    email: str,
    password: str,
    db: Session
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    # Check both the email and password before allowing login.
    if not user or not verify_password(
        password,
        user.hashed_password
    ):

        logger.warning("Failed login attempt")

        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    # Inactive accounts are not allowed to log in.
    if not user.is_active:

        raise HTTPException(
            status_code=403,
            detail="Account is inactive"
        )

    logger.info("Successful login: id=%s", user.id)

    return user


# CREATE ITEM

def create_item(
    item_data: ItemCreate,
    current_user: User,
    db: Session
):

    # Associate the new item with the currently logged-in user.
    item = Item(
        title=item_data.title,
        owner_id=current_user.id
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


# GET CURRENT USER ITEMS

def get_user_items(
    current_user: User,
    db: Session
):

    # Return only the items belonging to the current user.
    return db.query(Item).filter(
        Item.owner_id == current_user.id
    ).all()


# GET SINGLE ITEM

def get_item(
    item_id: int,
    current_user: User,
    db: Session
):

    # Check both the item ID and its owner to prevent unauthorized access.
    item = db.query(Item).filter(
        Item.id == item_id,
        Item.owner_id == current_user.id
    ).first()

    if not item:

        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


# UPDATE ITEM

def update_item(
    item_id: int,
    item_data: ItemUpdate,
    current_user: User,
    db: Session
):

    # Reuse the ownership check before updating the item.
    item = get_item(
        item_id,
        current_user,
        db
    )

    item.title = item_data.title

    db.commit()
    db.refresh(item)

    return item


# DELETE ITEM

def delete_item(
    item_id: int,
    current_user: User,
    db: Session
):

    # Make sure the item belongs to the current user before deleting it.
    item = get_item(
        item_id,
        current_user,
        db
    )

    db.delete(item)
    db.commit()

    return {
        "message": "Item deleted successfully"
    }