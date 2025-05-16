from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.auth.dependencies import get_current_user
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
def create_category_endpoint(category_data: CategoryCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    existing_category = get_category_by_name_type_user(db, category_data.name, category_data.type, current_user)
    if existing_category:
        raise HTTPException(status_code=400, detail="Category with this name and type already exists for the user.")
    return create_category(db, current_user, category_data)

@router.get("/", response_model=List[CategoryResponse])
def get_all_categories_endpoint(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    return get_all_categories(db,  current_user)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_single_category_endpoint(category_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    category = get_category_by_id(db, current_user, category_id)
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")
    return category
