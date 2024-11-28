from fastapi import FastAPI
from todo2 import todo_router
app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "hello world"}

app.include_router(todo_router)
# uvicorn test_api:app --port 8000 --reload
