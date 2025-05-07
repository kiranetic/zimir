from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.users.schemas import UserCreate, UserResponse
from app.users.crud import (
    create_user,
    get_user_by_email,
    get_user_by_id,
    get_all_users
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[UserResponse])
def get_all_users_endpoint(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.post("/", response_model=UserResponse)
def create_user_endpoint(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(db, user_data)

@router.get("/{user_id}", response_model=UserResponse)
def get_single_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user
