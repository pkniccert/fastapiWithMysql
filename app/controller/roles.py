from sqlalchemy.orm import Session
from app.models.user import User, Role, Permission
from app.schemas.user import RoleCreate


def create_role(db: Session, role: RoleCreate):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
