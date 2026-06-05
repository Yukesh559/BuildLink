"""API v1 routes"""
from fastapi import APIRouter
from .endpoints import auth, users, jobs

router = APIRouter(prefix="/api/v1")

router.include_router(auth.router, tags=["Authentication"])
router.include_router(users.router, tags=["Users"])
router.include_router(jobs.router, tags=["Jobs"])

__all__ = ["router"]
