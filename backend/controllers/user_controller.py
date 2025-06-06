from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dtos.user_dto import UserCreateDto
from db.database import get_db
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.list_users()


@router.post("/register")
def register_user(user: UserCreateDto, db: Session = Depends(get_db)):
    service = UserService(db)
    created_user = service.create_user(user)
    return {"status": 200, "message": "created"}
