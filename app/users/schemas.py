from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr = Field(...)

class UserCreate(UserBase):
    password: str = Field(...)

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes=True
