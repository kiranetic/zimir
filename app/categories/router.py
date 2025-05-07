from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.categories.schemas import CategoryCreate, CategoryResponse
from app.categories.crud import (
    create_category, 
    get_all_categories, 
    get_category_by_id, 
    get_category_by_name_type_user
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/", response_model=CategoryResponse)
def create_category_endpoint(category_data: CategoryCreate, db: Session = Depends(get_db), user_id: int = 1):
    existing_category = get_category_by_name_type_user(db, category_data.name, category_data.type, user_id)
    if existing_category:
        raise HTTPException(status_code=400, detail="Category with this name and type already exists for the user.")
    return create_category(db, user_id, category_data)

@router.get("/", response_model=List[CategoryResponse])
def get_all_categories_endpoint(db: Session = Depends(get_db), user_id: int = 1):
    return get_all_categories(db, user_id)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_single_category_endpoint(category_id: int, db: Session = Depends(get_db), user_id: int = 1):
    category = get_category_by_id(db, user_id, category_id)
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")
    return category
