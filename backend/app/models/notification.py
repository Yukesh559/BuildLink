"""Notification Pydantic models"""
from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class NotificationResponse(BaseModel):
    """Notification response"""
    id: UUID
    user_id: UUID
    notification_type: str
    title: str
    message: str
    related_id: Optional[UUID] = None
    is_read: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
