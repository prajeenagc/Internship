from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):

    __tablename__ = "users"

    # Primary key for each user.
    id = Column(Integer, primary_key=True, index=True)

    # Each user must have a unique username and email.
    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    # Store the hashed password instead of the original password.
    hashed_password = Column(
        String,
        nullable=False
    )

    # New users are active by default.
    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )

    # Allows access to all items belonging to this user.
    items = relationship(
        "Item",
        back_populates="owner"
    )


class Item(Base):

    __tablename__ = "items"

    # Primary key for each item.
    id = Column(Integer, primary_key=True, index=True)

    title = Column(
        String(100),
        nullable=False
    )

    # Links each item to the user who created it.
    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    # Allows access to the user who owns this item.
    owner = relationship(
        "User",
        back_populates="items"
    )