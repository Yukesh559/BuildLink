"""Admin Log ORM Model"""
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database.database import Base


class AdminLog(Base):
    """Admin action log model"""
    
    __tablename__ = "admin_logs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    admin_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    action = Column(String(255), nullable=False)  # user_blocked, job_deleted, payment_refunded, etc.
    target_type = Column(String(50), nullable=True)  # user, job, payment, bid
    target_id = Column(UUID(as_uuid=True), nullable=True)
    reason = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)
    
    def __repr__(self):
        return f"<AdminLog(id={self.id}, admin_id={self.admin_id}, action={self.action})>"
