from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import RoleCreate
from app.controller.users import Role
from app.dependencies.auth import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.create_role(db, role)

