from fastapi import APIRouter
from .v1 import roles, permissions, users

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(roles.router, prefix="/roles", tags=["roles"])
router.include_router(permissions.router, prefix="/permissions", tags=["permissions"])