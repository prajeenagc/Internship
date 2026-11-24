
from fastapi import FastAPI
from ariadne.asgi import GraphQL

from app.database import SessionLocal
from app import models
from app.schema import schema
from app.context import get_context_value


app = FastAPI()


@app.middleware("http")
async def manage_db_session(request, call_next):
    # Create a separate database session for each request.
    request.state.db = SessionLocal()

    try:
        response = await call_next(request)
        return response
    finally:
        # Close the session after the request is completed.
        request.state.db.close()


# Create the Ariadne GraphQL application.
graphql_app = GraphQL(
    schema,
    context_value=get_context_value
)

# Mount GraphQL at /graphql.
app.mount("/graphql", graphql_app)
