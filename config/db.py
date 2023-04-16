from pymongo import MongoClient

client = MongoClient("mongodb+srv://cglv11:4AM49MY5davDItig@cluster-python-crud.tkv0lxg.mongodb.net/?retryWrites=true&w=majority")

# NOMBRE DE LA DB
db = client.todo_application

# NOMBRE DE LA APLICACIÓN
collection_name = db["todos_app"]