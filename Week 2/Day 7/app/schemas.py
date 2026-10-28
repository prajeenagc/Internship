
from pydantic import BaseModel, Field

# task creation schema
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = ""

# created task response
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool
