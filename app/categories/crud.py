from sqlalchemy.orm import Session
from app.categories.models import Category
from app.categories.schemas import CategoryCreate
from typing import List, Optional

def create_category(db: Session, user_id: int, category_data: CategoryCreate) -> Category:
    new_category = Category(user_id=user_id, **category_data.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all_categories(db: Session, user_id: int) -> List[Category]:
    return db.query(Category).filter(Category.user_id == user_id).all()

def get_category_by_id(db: Session, user_id: int, category_id: int) -> Optional[Category]:
    return db.query(Category).filter(Category.user_id == user_id, Category.id == category_id).first()

def get_category_by_name_type_user(db: Session, name: str, type: str, user_id: int):
    return db.query(Category).filter(Category.name == name, Category.type == type, Category.user_id == user_id).first()
