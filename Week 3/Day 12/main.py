from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Task
from repository import create_task,get_tasks

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.post("/tasks")
def create_task_route(
    title:str,
    description: str=None,
    db:Session=Depends(get_db)
):
    return create_task(db,title,description)

@app.get("/tasks")
def get_tasks_route(db:Session=Depends(get_db)):
    return get_tasks(db)