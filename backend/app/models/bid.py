"""Bid Pydantic models"""
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class BidCreate(BaseModel):
    """Create bid request"""
    job_id: UUID
    bid_amount: float = Field(..., gt=0)
    bid_message: Optional[str] = None
    proposed_timeline_days: Optional[int] = None


class BidResponse(BaseModel):
    """Bid response"""
    id: UUID
    job_id: UUID
    worker_id: UUID
    bid_amount: float
    bid_message: Optional[str] = None
    proposed_timeline_days: Optional[int] = None
    bid_status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
