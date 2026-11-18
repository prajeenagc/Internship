from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Day 18 Authentication API"}