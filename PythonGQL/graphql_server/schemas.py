import strawberry

@strawberry.type
class Task:
    id:int
    content:str
    is_done:bool=False
