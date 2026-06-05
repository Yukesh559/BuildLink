"""Job service for business logic"""
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from uuid import UUID

from app.schemas.job import Job
from app.models import JobCreate, JobResponse, JobUpdate, JobListResponse
from app.core.constants import JOB_STATUS_OPEN
from app.utils.validators import validate_budget
from app.utils.logger import logger


class JobService:
    """Service for job operations"""

    @staticmethod
    def create_job(db: Session, owner_id: UUID, job_data: JobCreate) -> Job:
        """
        Create a new job
        
        Args:
            db: Database session
            owner_id: UUID of job owner
            job_data: Job creation data
            
        Returns:
            Created Job object
            
        Raises:
            ValueError: If budget validation fails
        """
        if not validate_budget(job_data.budget_min, job_data.budget_max):
            raise ValueError("Invalid budget: min must be <= max and both > 0")

        new_job = Job(
            owner_id=owner_id,
            title=job_data.title,
            description=job_data.description,
            category=job_data.category,
            budget_min=job_data.budget_min,
            budget_max=job_data.budget_max,
            location=job_data.location,
            latitude=job_data.latitude,
            longitude=job_data.longitude,
            images_urls=job_data.images_urls,
            required_skills=job_data.required_skills,
            timeline_days=job_data.timeline_days,
            job_status=JOB_STATUS_OPEN,
        )

        db.add(new_job)
        db.commit()
        db.refresh(new_job)

        logger.info(f"Job created: {new_job.id} by owner {owner_id}")
        return new_job

    @staticmethod
    def get_job(db: Session, job_id: UUID) -> Optional[Job]:
        """
        Get job by ID
        
        Args:
            db: Database session
            job_id: Job UUID
            
        Returns:
            Job object or None if not found
        """
        return db.query(Job).filter(Job.id == job_id).first()

    @staticmethod
    def get_user_jobs(db: Session, owner_id: UUID, skip: int = 0, limit: int = 10) -> tuple[List[Job], int]:
        """
        Get jobs for a specific owner
        
        Args:
            db: Database session
            owner_id: Owner UUID
            skip: Number of records to skip (pagination)
            limit: Number of records to return
            
        Returns:
            Tuple of (jobs list, total count)
        """
        total = db.query(Job).filter(Job.owner_id == owner_id).count()
        jobs = (
            db.query(Job)
            .filter(Job.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return jobs, total

    @staticmethod
    def list_jobs(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        category: Optional[str] = None,
        status: Optional[str] = None,
        location: Optional[str] = None,
    ) -> tuple[List[Job], int]:
        """
        List all jobs with optional filters
        
        Args:
            db: Database session
            skip: Number of records to skip
            limit: Number of records to return
            category: Filter by category
            status: Filter by job status
            location: Filter by location
            
        Returns:
            Tuple of (jobs list, total count)
        """
        query = db.query(Job)

        # Apply filters
        filters = []
        if category:
            filters.append(Job.category == category)
        if status:
            filters.append(Job.job_status == status)
        if location:
            filters.append(Job.location.ilike(f"%{location}%"))

        if filters:
            query = query.filter(and_(*filters))

        total = query.count()
        jobs = query.offset(skip).limit(limit).all()

        return jobs, total

    @staticmethod
    def update_job(db: Session, job_id: UUID, job_data: JobUpdate) -> Optional[Job]:
        """
        Update a job
        
        Args:
            db: Database session
            job_id: Job UUID
            job_data: Updated job data
            
        Returns:
            Updated Job object or None if not found
        """
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            return None

        # Update only provided fields
        if job_data.title:
            job.title = job_data.title
        if job_data.description:
            job.description = job_data.description
        if job_data.category:
            job.category = job_data.category
        if job_data.budget_min is not None and job_data.budget_max is not None:
            if validate_budget(job_data.budget_min, job_data.budget_max):
                job.budget_min = job_data.budget_min
                job.budget_max = job_data.budget_max
        if job_data.location:
            job.location = job_data.location
        if job_data.job_status:
            job.job_status = job_data.job_status
        if job_data.required_skills is not None:
            job.required_skills = job_data.required_skills
        if job_data.timeline_days is not None:
            job.timeline_days = job_data.timeline_days

        db.commit()
        db.refresh(job)

        logger.info(f"Job updated: {job_id}")
        return job

    @staticmethod
    def delete_job(db: Session, job_id: UUID) -> bool:
        """
        Delete a job
        
        Args:
            db: Database session
            job_id: Job UUID
            
        Returns:
            True if deleted, False if not found
        """
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            return False

        db.delete(job)
        db.commit()

        logger.info(f"Job deleted: {job_id}")
        return True

    @staticmethod
    def search_jobs(
        db: Session,
        query_text: str,
        skip: int = 0,
        limit: int = 10,
    ) -> tuple[List[Job], int]:
        """
        Search jobs by title or description
        
        Args:
            db: Database session
            query_text: Search query
            skip: Number of records to skip
            limit: Number of records to return
            
        Returns:
            Tuple of (jobs list, total count)
        """
        search_filter = or_(
            Job.title.ilike(f"%{query_text}%"),
            Job.description.ilike(f"%{query_text}%"),
        )

        total = db.query(Job).filter(search_filter).count()
        jobs = (
            db.query(Job)
            .filter(search_filter)
            .offset(skip)
            .limit(limit)
            .all()
        )

        return jobs, total
