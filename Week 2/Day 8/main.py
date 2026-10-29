
from fastapi import FastAPI, HTTPException, status
from schemas import TaskCreate, TaskResponse, TaskUpdate
from services import task_services

app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "Task API is running"}


# Create a task
@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    return task_services.create_task(task_data)


# Get all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks():
    return task_services.get_all_tasks()


# Get one task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = task_services.get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


# Update a task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate):
    task = task_services.update_task(task_id, task_data)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


# Delete a task
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    task = task_services.delete_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return None
