from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.models import User
from app.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)

from app.services.task_services import (
    create_task,
    update_task,
    delete_task,
    TaskServiceError
)


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# -----------------------------
# CREATE
# -----------------------------

@router.post("/", response_model=TaskResponse)
def create_task_route(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        task = create_task(
            db,
            task_data.model_dump(),
            current_user
        )

        return task

    except TaskServiceError as error:

        raise HTTPException(
            status_code=error.status_code,
            detail=error.message
        )


# -----------------------------
# UPDATE
# -----------------------------

@router.put("/{task_id}", response_model=TaskResponse)
def update_task_route(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        task = update_task(
            db,
            task_id,
            task_data.model_dump(exclude_unset=True),
            current_user
        )

        return task

    except TaskServiceError as error:

        raise HTTPException(
            status_code=error.status_code,
            detail=error.message
        )


# -----------------------------
# DELETE
# -----------------------------

@router.delete("/{task_id}")
def delete_task_route(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        result = delete_task(
            db,
            task_id,
            current_user
        )

        return result

    except TaskServiceError as error:

        raise HTTPException(
            status_code=error.status_code,
            detail=error.message
        )