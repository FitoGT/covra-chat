from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserRegisterRequestDto(BaseModel):
    name: str
    lastname: str
    email: EmailStr
    password: str


class UserDto(BaseModel):
    id: UUID
    name: str
    lastname: str
    email: EmailStr
    model_config = {
        "from_attributes": True
    }


class UserRegisterResponseDto(BaseModel):
    status: int
    message: str
    user: UserDto
    access_token: str
    token_type: str
