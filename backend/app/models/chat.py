"""Chat Pydantic models"""
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class ChatCreate(BaseModel):
    """Create chat message request"""
    receiver_id: UUID
    message: str
    job_id: Optional[UUID] = None


class ChatResponse(BaseModel):
    """Chat message response"""
    id: UUID
    sender_id: UUID
    receiver_id: UUID
    message: str
    is_read: bool
    job_id: Optional[UUID] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class ChatHistory(BaseModel):
    """Chat history response"""
    total: int
    messages: List[ChatResponse]
