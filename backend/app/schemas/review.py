"""Review ORM Model"""
from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database.database import Base


class Review(Base):
    """Review and rating model"""
    
    __tablename__ = "reviews"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    reviewer_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    reviewed_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    rating = Column(Integer, nullable=False)  # 1-5
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # One review per job per reviewer
    __table_args__ = (UniqueConstraint("job_id", "reviewer_id", name="unique_review_per_reviewer_per_job"),)
    
    def __repr__(self):
        return f"<Review(id={self.id}, rating={self.rating}, reviewed_user={self.reviewed_user_id})>"
