from pydantic import BaseModel, ConfigDict, EmailStr, Field


# USER SCHEMAS

class UserCreate(BaseModel):

    username: str = Field(min_length=3, max_length=50)

    email: EmailStr


class UserResponse(BaseModel):

    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# PROJECT SCHEMAS

class ProjectCreate(BaseModel):

    name: str = Field(min_length=2, max_length=100)

    description: str | None = None


class ProjectResponse(BaseModel):

    id: int
    name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)


# TASK SCHEMAS

class TaskCreate(BaseModel):

    title: str = Field(min_length=1, max_length=100)

    description: str | None = None

    project_id: int

    assigned_user_id: int | None = None


class TaskUpdate(BaseModel):

    title: str | None = Field(default=None, min_length=1, max_length=100)

    description: str | None = None

    is_completed: bool | None = None

    project_id: int | None = None

    assigned_user_id: int | None = None


class TaskResponse(BaseModel):

    id: int
    title: str
    description: str | None
    is_completed: bool
    project_id: int
    assigned_user_id: int | None

    model_config = ConfigDict(from_attributes=True)