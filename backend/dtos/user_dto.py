from pydantic import BaseModel, EmailStr


class UserCreateDto(BaseModel):
    name: str
    lastname: str
    email: EmailStr
    password: str
