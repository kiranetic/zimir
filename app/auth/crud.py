from sqlalchemy.orm import Session
from app.users.utils import pwd_context
from app.users.crud import get_user_by_email
from app.auth.utils import create_access_token

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def verify_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user and verify_password(password, user.hashed_password):
        return user
    return None

def authenticate_user(db: Session, email: str, password: str):
    user = verify_user(db, email, password)
    if not user:
        return None
    return create_access_token(user.id)
