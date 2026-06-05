"""Bid ORM Model"""
from sqlalchemy import Column, String, Text, Float, Integer, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database.database import Base


class Bid(Base):
    """Worker bid on job model"""
    
    __tablename__ = "bids"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    worker_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    bid_amount = Column(Float, nullable=False)
    bid_message = Column(Text, nullable=True)
    proposed_timeline_days = Column(Integer, nullable=True)
    bid_status = Column(String(50), default="pending", index=True)  # pending, accepted, rejected, completed
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # One bid per worker per job
    __table_args__ = (UniqueConstraint("job_id", "worker_id", name="unique_bid_per_worker_per_job"),)
    
    def __repr__(self):
        return f"<Bid(id={self.id}, job_id={self.job_id}, worker_id={self.worker_id}, status={self.bid_status})>"
