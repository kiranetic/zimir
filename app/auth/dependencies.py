from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth.utils import verify_access_token
from app.auth.schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> int:
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    user_id: int = payload.get("user_id")
    return user_id
