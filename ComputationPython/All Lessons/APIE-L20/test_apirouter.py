from fastapi import APIRouter
router = APIRouter()
@router.get("/hello")
async def welcome()  -> dict:
    return {"message": "new hello world"}