from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dtos.user_dto import UserRegisterRequestDto, UserDto, UserRegisterResponseDto
from db.database import get_db
from services.user_service import UserService
from utils.auth import get_current_user
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def list_users(db: Session = Depends(get_db), current_user: UserDto = Depends(get_current_user),):
    service = UserService(db)
    return service.list_users()


@router.post("/register")
def register_user(user: UserRegisterRequestDto, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        result = service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return UserRegisterResponseDto(
        status=200,
        message="User created successfully",
        user=UserDto.model_validate(result["user"]),
        access_token=result["token"],
        token_type="bearer",
    )
