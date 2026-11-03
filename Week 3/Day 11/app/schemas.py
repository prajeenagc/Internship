
from pydantic import BaseModel, ConfigDict




class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)



class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    created_by: int


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    created_by: int

    model_config = ConfigDict(from_attributes=True)



class ProjectMemberCreate(BaseModel):
    project_id: int
    user_id: int
    role: str = "member"


class ProjectMemberResponse(BaseModel):
    project_id: int
    user_id: int
    role: str

    model_config = ConfigDict(from_attributes=True)




class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    project_id: int
    owner_id: int | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    project_id: int
    owner_id: int | None

    model_config = ConfigDict(from_attributes=True)
