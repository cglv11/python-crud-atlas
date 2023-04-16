from fastapi import FastAPI
from routes.todos_routes import todo_api_router

app = FastAPI(
    title="REST API with FastAPI and mongodb Atlas",
    description="This is a simple rest api with fastAPI",
    version="0.0.1",
)

app.include_router(todo_api_router)