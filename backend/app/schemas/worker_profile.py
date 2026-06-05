"""Worker Profile ORM Model"""
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import uuid
from app.database.database import Base


class WorkerProfile(Base):
    """Worker profile model for additional worker information"""
    
    __tablename__ = "worker_profiles"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    skills = Column(ARRAY(String), nullable=False)  # ['carpentry', 'plumbing', ...]
    experience_years = Column(Integer, nullable=True)
    hourly_rate = Column(Float, nullable=True)
    availability_status = Column(String(50), default="available")  # available, busy, offline
    total_jobs_completed = Column(Integer, default=0)
    average_rating = Column(Float, default=0.0)
    is_verified = Column(Boolean, default=False)
    verification_document_url = Column(String(500), nullable=True)
    portfolio_urls = Column(ARRAY(String), nullable=True)  # ['url1', 'url2', ...]
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<WorkerProfile(user_id={self.user_id}, skills={self.skills}, rating={self.average_rating})>"
