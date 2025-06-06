from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from models.user import User
from dtos.user_dto import UserRegisterRequestDto
from utils.jwt_utils import create_access_token


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def list_users(self) -> list[User]:
        return self.repo.get_all_users()

    def create_user(self, user_data: UserRegisterRequestDto) -> User:
        user = self.repo.create_user(
            name=user_data.name,
            lastname=user_data.lastname,
            email=user_data.email,
            password=user_data.password,
        )
        token = create_access_token({"sub": str(user.id)})
        return {"user": user, "token": token}
