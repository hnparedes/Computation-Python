# Working with routing

# @app.get("/mem")
# async def memory_status():

# return ghs.get_memory()

#   json_compatible_item_data = jsonable_encoder(ghs.get_memory())
#   return JSONResponse(content=json_compatible_item_data)

# Routing example

# from fastapi import FastAPI
# from todo2 import todo_router
# app = FastAPI()


# @app.get("/")
# async def welcome() -> dict:
#     return {"message": "Hello World"}

# run with (venv)$ uvicorn test_api:app --port 8000 --reload

# APIRouting class

# test_apirouter.py
# from fastapi import APIRouter
# router = APIRouter()
# @router.get("/hello")
# async def say_hello() -> dict:
#     return {"message": "New Hello!"}

# uvicorn test_apirouter:router --port 8000 --reload

# From terminal: curl http://localhost:8000/hello
# From httpie http localhost:8000/hello

# APIRouting Creation & Testing

# todo.py
# from fastapi import APIRouter, Path

# todo_router = APIRouter()

# todo_list = []
# @todo_router.post("/todo")
# async def add_todo(todo: dict) -> dict:
#   todo_list.append(todo)
#   return {"message": "Todo added successfully"}

# @todo_router.get("/todo")
# async def retrieve_todos() -> dict:
#   return {"todos": todo_list}

# APIRouting Modified original Hello World

# from fastapi import FastAPI
# from todo import todo_router
# app = FastAPI()


# @app.get("/")
# async def welcome() -> dict:
#     return {"message": "Hello World"}
# app.include_router(todo_router)
# run with (venv)$ uvicorn test_api:app --port 8000 --reload
# curl -i http://localhost:8000/
# curl -X 'GET' 'http://localhost:8000/todo' -H 'accept: application/json'

# APIRouting Modified original and POST

# curl -X 'POST' 'http://localhost:8000/todo' - H 'accept: application/json' - H 'Content-
# Ty'{"id": 1, "item": "First Todo is to finish lecture"}'

# API Validation

# from pydantic import BaseModel
# class PacktBook(BaseModel):
#    id: int
#    Name: str
#    Publishers: str
#    Isbn: str
