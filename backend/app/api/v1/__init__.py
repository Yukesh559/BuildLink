"""API v1 routes"""
from fastapi import APIRouter
from .endpoints import auth, users

router = APIRouter(prefix="/api/v1")

router.include_router(auth.router, tags=["Authentication"])
router.include_router(users.router, tags=["Users"])

__all__ = ["router"]
