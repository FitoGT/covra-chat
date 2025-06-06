from sqlalchemy.orm import Session
from models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        return self.db.query(User).all()

    def create_user(self, name: str, lastname: str, email: str, password: str) -> User:
        hashed_password = pwd_context.hash(password)
        user = User(name=name, lastname=lastname,
                    email=email, password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
