from pydantic import BaseModel, Field, ConfigDict


class TaskCreate(BaseModel):

    title: str = Field(
        min_length=1,
        max_length=100
    )

    state: str = "pending"


class TaskUpdate(BaseModel):

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    state: str | None = None


class TaskResponse(BaseModel):

    id: int
    title: str
    state: str
    owner_id: int

    model_config = ConfigDict(
        from_attributes=True
    )