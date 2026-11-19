from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user, require_admin
from app.models import User
from app.schemas import TaskCreate, TaskResponse

from app.services import (
    create_task,
    get_task,
    update_task,
    delete_task
)

router = APIRouter()


# Creates a task for the current user.
@router.post("/tasks", response_model=TaskResponse)
def create(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_task(db, task_data, current_user)


# Gets a task belonging to the current user.
@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_task(db, task_id, current_user)


# Updates a task belonging to the current user.
@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update(
    task_id: int,
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_task(db, task_id, task_data, current_user)


# Deletes a task belonging to the current user.
@router.delete("/tasks/{task_id}")
def delete(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_task(db, task_id, current_user)


# Allows administrators to delete users.
@router.delete("/admin/users/{user_id}")
def admin_delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    # Finds the user that the administrator wants to delete.
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}