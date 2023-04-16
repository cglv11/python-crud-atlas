from fastapi import APIRouter, Response, status
from config.db import collection_name
from models.todos_model import Todo
from schemas.todos_schema import todo_serializer, todos_serializer
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

todo_api_router = APIRouter()

# RETRIEVE
@todo_api_router.get("/")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    return { "status": 200, "data": todos }

@todo_api_router.get("/{id}")
async def get_todo(id: str):
    todo = todos_serializer(collection_name.find({"_id": ObjectId(id)}))
    return { "status": 200, "data": todo }

@todo_api_router.post("/")
async def post_todo(todo: Todo):
    _id = collection_name.insert_one(dict(todo))
    todo = todos_serializer(collection_name.find({"_id": _id.inserted_id}))
    return { "status": 200, "data": todo }

@todo_api_router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    todo = todos_serializer(collection_name.find({"_id": ObjectId(id)}))
    return { "status": 200, "data": todo }

@todo_api_router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": 200, "data": []}