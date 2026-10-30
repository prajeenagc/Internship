from fastapi import FastAPI
from middleware  import request_middleware
from errors import AppError, app_error_handler
from fastapi import BackgroundTasks
from audit import record_audit
import logging 
logging.basicConfig(level=logging.INFO)


app=FastAPI()
app.add_exception_handler(AppError, app_error_handler)
app.middleware("http")(request_middleware)


@app.get("/")
def home():
    return{"message":"Application is running"}

@app.get("/tasks")
def get_tasks(background_tasks: BackgroundTasks):
    background_tasks.add_task(record_audit, "Tasks endpoint accessed")

    return {"tasks": ["Study", "Eat", "Dance"]}

@app.get("/test-error")
def test_error():
    raise AppError("This is a test error", "TEST_ERROR")

