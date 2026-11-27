from sqlalchemy.orm import Session

from app.models import Task, User


ALLOWED_STATES = [
    "pending",
    "in_progress",
    "completed"
]


class TaskServiceError(Exception):

    def __init__(
        self,
        message: str,
        status_code: int = 400
    ):

        self.message = message
        self.status_code = status_code

        super().__init__(message)


# -----------------------------
# VALIDATION
# -----------------------------

def validate_title(title: str):

    if not title or not title.strip():

        raise TaskServiceError(
            "Title cannot be empty"
        )

    if len(title) > 100:

        raise TaskServiceError(
            "Title cannot exceed 100 characters"
        )


def validate_state(state: str):

    if state not in ALLOWED_STATES:

        raise TaskServiceError(
            "Invalid state. Allowed states: pending, in_progress, completed"
        )


# -----------------------------
# OWNERSHIP CHECK
# -----------------------------

def get_owned_task(
    db: Session,
    task_id: int,
    current_user: User
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        raise TaskServiceError(
            "Task not found",
            status_code=404
        )

    if task.owner_id != current_user.id:

        raise TaskServiceError(
            "You do not have permission to access this task",
            status_code=403
        )

    return task


# -----------------------------
# CREATE TASK
# -----------------------------

def create_task(
    db: Session,
    task_data: dict,
    current_user: User
):

    title = task_data["title"]
    state = task_data["state"]

    validate_title(title)
    validate_state(state)

    new_task = Task(
        title=title.strip(),
        state=state,
        owner_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# -----------------------------
# UPDATE TASK
# -----------------------------

def update_task(
    db: Session,
    task_id: int,
    task_data: dict,
    current_user: User
):

    task = get_owned_task(
        db,
        task_id,
        current_user
    )

    if "title" in task_data:

        validate_title(task_data["title"])

        task.title = task_data["title"].strip()

    if "state" in task_data:

        validate_state(task_data["state"])

        task.state = task_data["state"]

    db.commit()
    db.refresh(task)

    return task


# -----------------------------
# DELETE TASK
# -----------------------------

def delete_task(
    db: Session,
    task_id: int,
    current_user: User
):

    task = get_owned_task(
        db,
        task_id,
        current_user
    )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully",
        "task_id": task_id
    }