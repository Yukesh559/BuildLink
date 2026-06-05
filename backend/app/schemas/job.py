"""Job ORM Model"""
from sqlalchemy import Column, String, Text, Float, Integer, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import uuid
from app.database.database import Base


class Job(Base):
    """Job posting model"""
    
    __tablename__ = "jobs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(100), nullable=False, index=True)
    budget_min = Column(Float, nullable=False)
    budget_max = Column(Float, nullable=False)
    location = Column(String(255), nullable=False, index=True)
    latitude = Column(String(50), nullable=True)
    longitude = Column(String(50), nullable=True)
    job_status = Column(String(50), default="open", index=True)  # open, in_progress, completed, cancelled
    images_urls = Column(ARRAY(String), nullable=True)  # ['url1', 'url2', ...]
    required_skills = Column(ARRAY(String), nullable=True)  # ['carpentry', 'plumbing', ...]
    timeline_days = Column(Integer, nullable=True)
    winner_bid_id = Column(UUID(as_uuid=True), nullable=True)  # Reference to accepted bid
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title}, status={self.job_status})>"
