from fastapi import FastAPI

from app.routes import router


# Creates the FastAPI application.
app = FastAPI(
    title="Day 19 - Ownership and Roles",
    description="Task ownership and role-based authorization",
    version="1.0.0"
)

# Registers the application routes.
app.include_router(router)