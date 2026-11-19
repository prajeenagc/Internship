from pydantic import BaseModel, Field, ConfigDict


#schema for validating incoming task creation data
class TaskCreate(BaseModel):
    title: str=Field(min_length=3,max_length=100)


#schema for defining the structure of response
class TaskResponse(BaseModel):
    id:int
    title:str
    is_completed:bool
    owner_id: int


    #allows pydantic to read data directly from SQLAlchemy model attributes
    model_config=ConfigDict(from_attributes=True)