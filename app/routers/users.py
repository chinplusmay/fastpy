from fastapi import APIRouter
from app.schemas.user_schema import User

router = APIRouter()


@router.get("/users/{user_id}")
def getUser(user_id : int):
    return {"user_id" : user_id}

@router.post("/users") 
def create_user(user: User):
    return {"user": user}