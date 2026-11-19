from sqlalchemy import Column,String,Boolean,Integer,Text,ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


#defines user table in the database
class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    role = Column(String(20), default="user", nullable=False)


    #defines relationship between User and Task
    tasks=relationship("Task",back_populates="owner")


#defines task table in the database
class Task(Base):
    __tablename__="tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    is_completed = Column(Boolean, default=False)

    owner_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    
    #defines relationship between User and Task
    owner=relationship("User",back_populates="tasks")