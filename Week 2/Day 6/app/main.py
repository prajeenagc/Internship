from fastapi import FastAPI


app=FastAPI()

tasks = ["study", "eat", "exercise", "read"]

@app.get("/health")
def health_status():
    return{"status":"healthy"}


@app.get("/tasks")
def task():
    return tasks