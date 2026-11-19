from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Task, User


# Creates a new task for the current user.
def create_task(db: Session, task_data, current_user: User):

    task = Task(
        title=task_data.title,
        owner_id=current_user.id  # Assigns the task to its owner.
    )

    db.add(task)       # Adds the task to the database session.
    db.commit()        # Saves the changes to the database.
    db.refresh(task)   # Refreshes the task with the saved database values.

    return task


# Gets a task only if it belongs to the current user.
def get_task(db: Session, task_id: int, current_user: User):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# Updates the title of an existing task.
def update_task(
    db: Session,
    task_id: int,
    task_data,
    current_user: User
):

    task = get_task(db, task_id, current_user)

    task.title = task_data.title

    db.commit()
    db.refresh(task)

    return task


# Deletes a task belonging to the current user.
def delete_task(db: Session, task_id: int, current_user: User):

    task = get_task(db, task_id, current_user)

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}