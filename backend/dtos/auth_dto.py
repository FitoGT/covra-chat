from pydantic import BaseModel, EmailStr


class LoginRequestDto(BaseModel):
    email: EmailStr
    password: str


class LoginResponseDto(BaseModel):
    access_token: str
    token_type: str
