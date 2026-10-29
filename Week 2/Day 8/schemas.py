from pydantic import BaseModel,Field

#creating schema for task creation
class TaskCreate(BaseModel):
    title:str=Field(min_length=1,max_length=100)
    description:str=""

#creating schema for task response
class TaskResponse(BaseModel):
    id:int
    title:str
    description:str
    is_done:bool

#creating schema for updating task
class TaskUpdate(BaseModel):
    title:str=Field(min_length=1,max_length=100)
    description:str=""
    is_done:bool