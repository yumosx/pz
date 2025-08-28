from fastapi import APIRouter
from api.service.user_service import UserService


router = APIRouter()

@router.post("/register")
def register():
    return

@router.get("/user_info/{user_id}")
def get_user_info(user_id: int):
    UserService.get_user_info(None, user_id)
    return