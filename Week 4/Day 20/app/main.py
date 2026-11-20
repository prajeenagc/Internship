import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router
from app.config import settings


# Set up logging so we can track important events and errors.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Create the FastAPI application.
app = FastAPI(
    title="Day 20 - Security Review",
    description="Authentication and ownership security testing"
)


# Configure CORS to allow requests only from trusted frontend origins.
app.add_middleware(
    CORSMiddleware,

    # Only allow frontend URLs defined in our configuration.
    allow_origins=settings.TRUSTED_ORIGINS,

    # Allow cookies and authentication credentials in cross-origin requests.
    allow_credentials=True,

    # Specify which HTTP methods the frontend can use.
    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],

    # Allow the headers needed for API requests and authentication.
    allow_headers=[
        "Authorization",
        "Content-Type"
    ]
)


# A simple route to check whether the API is running.
@app.get("/")
def home():

    return {
        "message": "Security Review API is running"
    }


# Register all application routes with the main FastAPI app.
app.include_router(router)