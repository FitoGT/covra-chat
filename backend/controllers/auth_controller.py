from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from dtos.auth_dto import LoginRequestDto, LoginResponseDto
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponseDto)
def login(request: LoginRequestDto, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    print('entre')
    token = auth_service.authenticate_user(request.email, request.password)
    return {"access_token": token, "token_type": "bearer"}
