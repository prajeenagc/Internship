from graphql import GraphQLError

from app.models import Task


def resolve_current_user(_, info):
    # Get the authenticated user from the request context.
    user = info.context["current_user"]

    if user is None:
        raise GraphQLError("Authentication required")

    return user


def resolve_my_tasks(_, info):
    # Get the authenticated user and database session.
    user = info.context["current_user"]
    db = info.context["db"]

    if user is None:
        raise GraphQLError("Authentication required")

    # Only return tasks belonging to the current user.
    return db.query(Task).filter(
        Task.owner_id == user.id
    ).all()