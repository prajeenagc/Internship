from app.database import SessionLocal
from app.models import User

from app.services.task_services import (
    create_task,
    update_task,
    delete_task,
    TaskServiceError
)


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def get_user_from_context(info):

    request = info.context["request"]

    user_id = request.headers.get("X-User-ID")

    if not user_id or not user_id.isdigit():

        return None

    db = info.context["db"]

    user = db.query(User).filter(
        User.id == int(user_id)
    ).first()

    return user


def error_result(message):

    return {
        "success": False,
        "message": message,
        "task": None,
        "taskId": None
    }


# -----------------------------
# CREATE MUTATION
# -----------------------------

def resolve_create_task(
    _,
    info,
    title,
    state="pending"
):

    db = info.context["db"]

    current_user = get_user_from_context(info)

    if not current_user:

        return error_result(
            "Authentication required"
        )

    try:

        task = create_task(
            db,
            {
                "title": title,
                "state": state
            },
            current_user
        )

        return {
            "success": True,
            "message": "Task created successfully",
            "task": task,
            "taskId": task.id
        }

    except TaskServiceError as error:

        return error_result(error.message)


# -----------------------------
# UPDATE MUTATION
# -----------------------------

def resolve_update_task(
    _,
    info,
    taskId,
    title=None,
    state=None
):

    db = info.context["db"]

    current_user = get_user_from_context(info)

    if not current_user:

        return error_result(
            "Authentication required"
        )

    task_data = {}

    if title is not None:

        task_data["title"] = title

    if state is not None:

        task_data["state"] = state

    try:

        task = update_task(
            db,
            taskId,
            task_data,
            current_user
        )

        return {
            "success": True,
            "message": "Task updated successfully",
            "task": task,
            "taskId": task.id
        }

    except TaskServiceError as error:

        return error_result(error.message)


# -----------------------------
# DELETE MUTATION
# -----------------------------

def resolve_delete_task(
    _,
    info,
    taskId
):

    db = info.context["db"]

    current_user = get_user_from_context(info)

    if not current_user:

        return error_result(
            "Authentication required"
        )

    try:

        result = delete_task(
            db,
            taskId,
            current_user
        )

        return {
            "success": True,
            "message": result["message"],
            "task": None,
            "taskId": result["task_id"]
        }

    except TaskServiceError as error:

        return error_result(error.message)