from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import get_users, create_user

router = APIRouter()

@router.get("/", response_model=list[User])
async def list_users():
    return get_users()

@router.post("/", response_model=User)
async def add_user(user: User):
    return create_user(user)
