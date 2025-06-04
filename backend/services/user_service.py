from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from models.user import User


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def list_users(self) -> list[User]:
        return self.repo.get_all_users()
