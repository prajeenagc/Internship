from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import text

from app.database import get_db
from app import models, schemas


app = FastAPI(
    title="Day 15 Database Integration API",
    description="FastAPI with PostgreSQL and SQLAlchemy",
    version="1.0.0"
)



def check_integrity_error(db: Session):

    db.rollback()

    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Database constraint violation. Check duplicate values or references."
    )



@app.get("/health")
def health_check(db: Session = Depends(get_db)):

    try:

        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(
            status_code=503,
            detail="Database connection failed"
        )




@app.post(
    "/users",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user_data: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(models.User).filter(
        models.User.email == user_data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    new_user = models.User(
        username=user_data.username,
        email=user_data.email
    )

    try:

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    except IntegrityError:

        check_integrity_error(db)


@app.get(
    "/users",
    response_model=list[schemas.UserResponse]
)
def get_users(db: Session = Depends(get_db)):

    return db.query(models.User).all()



@app.post(
    "/projects",
    response_model=schemas.ProjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_project(
    project_data: schemas.ProjectCreate,
    db: Session = Depends(get_db)
):

    existing_project = db.query(models.Project).filter(
        models.Project.name == project_data.name
    ).first()

    if existing_project:
        raise HTTPException(
            status_code=409,
            detail="Project already exists"
        )

    new_project = models.Project(
        name=project_data.name,
        description=project_data.description
    )

    try:

        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        return new_project

    except IntegrityError:

        check_integrity_error(db)


@app.get(
    "/projects",
    response_model=list[schemas.ProjectResponse]
)
def get_projects(db: Session = Depends(get_db)):

    return db.query(models.Project).all()




@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task_data: schemas.TaskCreate,
    db: Session = Depends(get_db)
):

    project = db.query(models.Project).filter(
        models.Project.id == task_data.project_id
    ).first()

    if not project:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    if task_data.assigned_user_id is not None:

        user = db.query(models.User).filter(
            models.User.id == task_data.assigned_user_id
        ).first()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="Assigned user not found"
            )

    new_task = models.Task(
        title=task_data.title,
        description=task_data.description,
        project_id=task_data.project_id,
        assigned_user_id=task_data.assigned_user_id
    )

    try:

        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        return new_task

    except IntegrityError:

        check_integrity_error(db)


@app.get(
    "/tasks",
    response_model=list[schemas.TaskResponse]
)
def get_tasks(db: Session = Depends(get_db)):

    return db.query(models.Task).all()


@app.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.patch(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def update_task(
    task_id: int,
    task_data: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    update_data = task_data.model_dump(exclude_unset=True)

    if "project_id" in update_data and update_data["project_id"] is not None:

        project = db.query(models.Project).filter(
            models.Project.id == update_data["project_id"]
        ).first()

        if not project:

            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )

    if "assigned_user_id" in update_data and update_data["assigned_user_id"] is not None:

        user = db.query(models.User).filter(
            models.User.id == update_data["assigned_user_id"]
        ).first()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="Assigned user not found"
            )

    for key, value in update_data.items():

        setattr(task, key, value)

    try:

        db.commit()
        db.refresh(task)

        return task

    except IntegrityError:

        check_integrity_error(db)


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_200_OK
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }