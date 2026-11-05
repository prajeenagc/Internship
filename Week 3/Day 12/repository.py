from sqlalchemy.orm import Session
from models import Task

def create_task(db:Session,title:str,description:str):

    try:
        task=Task(
            title=title,
            description=description
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return task
    
    except Exception:
        db.rollback()
        raise

def get_tasks(db:Session):
    return db.query(Task).all()