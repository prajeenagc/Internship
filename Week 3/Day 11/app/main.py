
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas


app = FastAPI(
    title="Day 11 PostgreSQL Lab"
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
    user = models.User(
        name=user_data.name,
        email=user_data.email
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@app.get(
    "/users",
    response_model=list[schemas.UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):
    users = db.query(models.User).all()

    return users




@app.post(
    "/projects",
    response_model=schemas.ProjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_project(
    project_data: schemas.ProjectCreate,
    db: Session = Depends(get_db)
):
    creator = db.query(models.User).filter(
        models.User.id == project_data.created_by
    ).first()

    if creator is None:
        raise HTTPException(
            status_code=404,
            detail="Creator user not found"
        )

    project = models.Project(
        name=project_data.name,
        description=project_data.description,
        created_by=project_data.created_by
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


@app.get(
    "/projects",
    response_model=list[schemas.ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db)
):
    projects = db.query(models.Project).all()

    return projects


# =====================================
# PROJECT MEMBERS
# =====================================

@app.post(
    "/project-members",
    response_model=schemas.ProjectMemberResponse,
    status_code=status.HTTP_201_CREATED
)
def add_project_member(
    member_data: schemas.ProjectMemberCreate,
    db: Session = Depends(get_db)
):
    project = db.query(models.Project).filter(
        models.Project.id == member_data.project_id
    ).first()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    user = db.query(models.User).filter(
        models.User.id == member_data.user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    member = models.ProjectMember(
        project_id=member_data.project_id,
        user_id=member_data.user_id,
        role=member_data.role
    )

    db.add(member)
    db.commit()
    db.refresh(member)

    return member


# =====================================
# TASKS
# =====================================

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

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    if task_data.owner_id is not None:
        owner = db.query(models.User).filter(
            models.User.id == task_data.owner_id
        ).first()

        if owner is None:
            raise HTTPException(
                status_code=404,
                detail="Task owner not found"
            )

    task = models.Task(
        title=task_data.title,
        description=task_data.description,
        project_id=task_data.project_id,
        owner_id=task_data.owner_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@app.get(
    "/tasks",
    response_model=list[schemas.TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db)
):
    tasks = db.query(models.Task).all()

    return tasks
