from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base


url=URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    database="mydb",
    port=5432
)

engine=create_engine(url)
Session=sessionmaker(bind=engine)
session=Session()


Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)

Base.metadata.create_all(engine)

app=FastAPI()

# @app.get("/")
# def home():
#     return{"message":"First FASTAPI app"}

@app.post("/create")
async def create_todo(text:str, is_complete:bool = False):
    todo=Todo(text=text,is_done=is_complete)
    session.add(todo)
    session.commit()
    return {"todo added": todo.text }

@app.get("/")
async def get_all_todos():
    todos_query=session.query(Todo)
    return todos_query.all()

@app.get("/done")
async def list_done_todos():
    todos_query=session.query(Todo)
    done_todos_list=todos_query.filter(Todo.is_done==True)
    return done_todos_list.all()


@app.put("/update/{id}")
async def update_todo(
    id:int,
    new_text:str="",
    is_complete:bool=False
):
    todo_query=session.query(Todo).filter(Todo.id==id)
    todo=todo_query.first()
    if new_text:
        todo.text=new_text # type: ignore
    todo.is_done=is_complete# type: ignore
    session.add(todo)
    session.commit

@app.delete("/delete/{id}")
async def delete_todo(id:int):
    todo_query=session.query(Todo)
    todo=todo_query.filter(Todo.id==id).first()
    session.delete(todo)
    session.commit()
    return{"Todo Deleted":todo.text}# type: ignore