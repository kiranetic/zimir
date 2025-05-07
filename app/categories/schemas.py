from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.categories.models import CategoryType

class CategoryBase(BaseModel):
    name: str = Field(..., max_length=50)
    description: Optional[str] = None
    type: CategoryType

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
