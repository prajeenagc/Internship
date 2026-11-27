from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from sqlalchemy.orm import Session
from ariadne.asgi import GraphQL

from app.database import Base, engine, SessionLocal
from app.models import User
from app.routes.task_routes import router
from app.graphql.schema import schema


# -----------------------------
# APPLICATION STARTUP
# -----------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Create demo users
    with SessionLocal() as db:

        if db.query(User).count() == 0:

            user1 = User(username="user1")
            user2 = User(username="user2")

            db.add_all([user1, user2])
            db.commit()

    yield


app = FastAPI(
    title="Day 23 - Shared Services",
    lifespan=lifespan
)


# -----------------------------
# REST ROUTES
# -----------------------------

app.include_router(router)


# -----------------------------
# GRAPHQL DATABASE SESSION
# -----------------------------

@app.middleware("http")
async def graphql_db_middleware(request: Request, call_next):

    if not request.url.path.startswith("/graphql"):

        return await call_next(request)

    db = SessionLocal()

    request.state.db = db

    try:

        response = await call_next(request)

        return response

    finally:

        db.close()


# -----------------------------
# GRAPHQL CONTEXT
# -----------------------------

def get_graphql_context(request, _data):

    return {
        "request": request,
        "db": request.state.db
    }


# -----------------------------
# GRAPHQL APPLICATION
# -----------------------------

graphql_app = GraphQL(
    schema,
    debug=True,
    context_value=get_graphql_context
)


app.mount(
    "/graphql",
    graphql_app
)


# -----------------------------
# HOME ROUTE
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "Day 23 Shared Services API is running"
    }