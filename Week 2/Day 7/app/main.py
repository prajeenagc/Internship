
from fastapi import FastAPI, status
from schemas import TaskCreate, TaskResponse

app = FastAPI()

# storing tasks in a list for now
tasks = []
next_id = 1


# home route
@app.get("/")
def home():
    return {"message": "Task API is running"}


# get all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks


# create a new task
@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):
    global next_id

    # creating the task with an id and default status
    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "is_done": False
    }

    # saving the task and updating the id
    tasks.append(new_task)
    next_id += 1

    return new_task
