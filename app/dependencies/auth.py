from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.core.auth import AuthService
from app.schemas.user import TokenData

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    auth_service = AuthService()
    user_data = auth_service.decode_access_token(token)
    if user_data is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user_data
