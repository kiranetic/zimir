from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.schemas import LoginRequest, Token
from app.auth.crud import verify_user
from app.db.session import get_db
from app.auth.crud import authenticate_user

router = APIRouter(tags=["Auth"])

@router.post("/", response_model=Token)
def login_endpoint(request: LoginRequest, db: Session = Depends(get_db)):
    token = authenticate_user(db, request.email, request.password)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
