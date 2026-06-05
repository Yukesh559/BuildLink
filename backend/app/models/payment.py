"""Payment Pydantic models"""
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class PaymentCreate(BaseModel):
    """Create payment request"""
    job_id: UUID
    amount: float = Field(..., gt=0)
    payment_method: str  # stripe, mock, upi
    stripe_token: Optional[str] = None  # For Stripe payments


class PaymentResponse(BaseModel):
    """Payment response"""
    id: UUID
    job_id: UUID
    payer_id: UUID
    payee_id: UUID
    amount: float
    payment_status: str
    payment_method: Optional[str] = None
    stripe_transaction_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
