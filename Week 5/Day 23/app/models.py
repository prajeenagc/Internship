from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String(50),
        nullable=False,
        unique=True
    )

    tasks = relationship(
        "Task",
        back_populates="owner"
    )


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(
        String(100),
        nullable=False
    )

    state = Column(
        String(30),
        nullable=False,
        default="pending"
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    owner = relationship(
        "User",
        back_populates="tasks"
    )