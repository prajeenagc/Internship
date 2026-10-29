from schemas import TaskCreate, TaskUpdate

# Temporary storage for tasks
tasks = []
next_id = 1


# Create a new task
def create_task(task_data: TaskCreate):
    global next_id

    task = {
        "id": next_id,
        "title": task_data.title,
        "description": task_data.description,
        "is_done": False
    }

    tasks.append(task)
    next_id += 1

    return task


# Get all tasks
def get_all_tasks():
    return tasks


# Get one task by ID
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


# Update an existing task
def update_task(task_id: int, task_data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_data.title
            task["description"] = task_data.description
            task["is_done"] = task_data.is_done

            return task

    return None


# Delete a task
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return task

    return None
