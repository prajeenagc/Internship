from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings


#creates db engine using database url. engine is used to make connection between application and database.
engine=create_engine(settings.DATABASE_URL)

#creates a session factory to interact with the database
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# base class for all SQLAlchemy database models.
Base=declarative_base()

#dependency function that provides a database session to all API endpoints
def get_db():
    db=SessionLocal()

    try:
        yield db

    finally:
        db.close()