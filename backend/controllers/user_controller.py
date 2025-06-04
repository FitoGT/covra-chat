from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from services.user_service import UserService
from repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.list_users()
