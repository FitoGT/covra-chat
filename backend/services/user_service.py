from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from models.user import User
from dtos.user_dto import UserCreateDto


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def list_users(self) -> list[User]:
        return self.repo.get_all_users()

    def create_user(self, user_data: UserCreateDto) -> User:
        return self.repo.create_user(
            name=user_data.name,
            lastname=user_data.lastname,
            email=user_data.email,
            password=user_data.password,
        )
