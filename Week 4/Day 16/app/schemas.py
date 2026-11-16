from pydantic import BaseModel, EmailStr, Field


# Registration input
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)


# Login input
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Public user response
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool


# Login response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str