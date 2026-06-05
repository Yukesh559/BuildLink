"""Job Pydantic models"""
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class JobCreate(BaseModel):
    """Create job request"""
    title: str = Field(..., min_length=5, max_length=255)
    description: str = Field(..., min_length=10)
    category: str
    budget_min: float = Field(..., gt=0)
    budget_max: float = Field(..., gt=0)
    location: str
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    images_urls: Optional[List[str]] = None
    required_skills: Optional[List[str]] = None
    timeline_days: Optional[int] = None


class JobUpdate(BaseModel):
    """Update job request"""
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    location: Optional[str] = None
    job_status: Optional[str] = None
    required_skills: Optional[List[str]] = None
    timeline_days: Optional[int] = None


class JobResponse(BaseModel):
    """Job response"""
    id: UUID
    owner_id: UUID
    title: str
    description: str
    category: str
    budget_min: float
    budget_max: float
    location: str
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    job_status: str
    images_urls: Optional[List[str]] = None
    required_skills: Optional[List[str]] = None
    timeline_days: Optional[int] = None
    winner_bid_id: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class JobListResponse(BaseModel):
    """Job list with pagination"""
    total: int
    page: int
    page_size: int
    jobs: List[JobResponse]
