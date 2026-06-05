"""Review Pydantic models"""
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class ReviewCreate(BaseModel):
    """Create review request"""
    job_id: UUID
    reviewed_user_id: UUID
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None


class ReviewResponse(BaseModel):
    """Review response"""
    id: UUID
    job_id: UUID
    reviewer_id: UUID
    reviewed_user_id: UUID
    rating: int
    comment: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
