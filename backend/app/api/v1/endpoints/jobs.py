"""Job endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from uuid import UUID

from app.database.database import get_db
from app.models import JobCreate, JobResponse, JobUpdate, JobListResponse
from app.middleware.auth import get_current_user, get_current_owner
from app.schemas.user import User
from app.services.job_service import JobService
from app.utils.logger import logger
from app.core.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE

router = APIRouter(prefix="/jobs")


@router.post("", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
async def create_job(
    job_data: JobCreate,
    current_user: User = Depends(get_current_owner),
    db: Session = Depends(get_db),
):
    """
    Create a new job posting
    
    Args:
        job_data: Job creation data
        current_user: Current authenticated owner user
        db: Database session
        
    Returns:
        Created JobResponse
        
    Raises:
        HTTPException: If validation fails
    """
    try:
        job = JobService.create_job(db, current_user.id, job_data)
        return JobResponse.from_orm(job)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except Exception as e:
        logger.error(f"Error creating job: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create job",
        )


@router.get("", response_model=JobListResponse)
async def list_jobs(
    skip: int = Query(0, ge=0),
    limit: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE),
    category: str = Query(None),
    status: str = Query(None),
    location: str = Query(None),
    db: Session = Depends(get_db),
):
    """
    List all jobs with optional filtering
    
    Args:
        skip: Number of records to skip (pagination)
        limit: Number of records to return
        category: Filter by category
        status: Filter by job status
        location: Filter by location
        db: Database session
        
    Returns:
        JobListResponse with paginated jobs
    """
    try:
        jobs, total = JobService.list_jobs(
            db,
            skip=skip,
            limit=limit,
            category=category,
            status=status,
            location=location,
        )
        return JobListResponse(
            total=total,
            page=skip // limit + 1,
            page_size=limit,
            jobs=[JobResponse.from_orm(job) for job in jobs],
        )
    except Exception as e:
        logger.error(f"Error listing jobs: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list jobs",
        )


@router.get("/{job_id}", response_model=JobResponse)
async def get_job(
    job_id: UUID,
    db: Session = Depends(get_db),
):
    """
    Get job by ID
    
    Args:
        job_id: Job UUID
        db: Database session
        
    Returns:
        JobResponse
        
    Raises:
        HTTPException: If job not found
    """
    try:
        job = JobService.get_job(db, job_id)
        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found",
            )
        return JobResponse.from_orm(job)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching job: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch job",
        )


@router.get("/me/jobs", response_model=JobListResponse)
async def get_my_jobs(
    skip: int = Query(0, ge=0),
    limit: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE),
    current_user: User = Depends(get_current_owner),
    db: Session = Depends(get_db),
):
    """
    Get current user's jobs (owner only)
    
    Args:
        skip: Number of records to skip
        limit: Number of records to return
        current_user: Current authenticated owner
        db: Database session
        
    Returns:
        JobListResponse with user's jobs
    """
    try:
        jobs, total = JobService.get_user_jobs(
            db,
            current_user.id,
            skip=skip,
            limit=limit,
        )
        return JobListResponse(
            total=total,
            page=skip // limit + 1,
            page_size=limit,
            jobs=[JobResponse.from_orm(job) for job in jobs],
        )
    except Exception as e:
        logger.error(f"Error fetching user jobs: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch your jobs",
        )


@router.put("/{job_id}", response_model=JobResponse)
async def update_job(
    job_id: UUID,
    job_data: JobUpdate,
    current_user: User = Depends(get_current_owner),
    db: Session = Depends(get_db),
):
    """
    Update a job (owner only)
    
    Args:
        job_id: Job UUID
        job_data: Updated job data
        current_user: Current authenticated owner
        db: Database session
        
    Returns:
        Updated JobResponse
        
    Raises:
        HTTPException: If job not found or user not authorized
    """
    try:
        job = JobService.get_job(db, job_id)
        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found",
            )

        # Check authorization
        if job.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only update your own jobs",
            )

        updated_job = JobService.update_job(db, job_id, job_data)
        return JobResponse.from_orm(updated_job)
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except Exception as e:
        logger.error(f"Error updating job: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update job",
        )


@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_job(
    job_id: UUID,
    current_user: User = Depends(get_current_owner),
    db: Session = Depends(get_db),
):
    """
    Delete a job (owner only)
    
    Args:
        job_id: Job UUID
        current_user: Current authenticated owner
        db: Database session
        
    Returns:
        None (204 No Content)
        
    Raises:
        HTTPException: If job not found or user not authorized
    """
    try:
        job = JobService.get_job(db, job_id)
        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found",
            )

        # Check authorization
        if job.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only delete your own jobs",
            )

        JobService.delete_job(db, job_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting job: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete job",
        )


@router.get("/search", response_model=JobListResponse)
async def search_jobs(
    q: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE),
    db: Session = Depends(get_db),
):
    """
    Search jobs by query text
    
    Args:
        q: Search query
        skip: Number of records to skip
        limit: Number of records to return
        db: Database session
        
    Returns:
        JobListResponse with search results
    """
    try:
        jobs, total = JobService.search_jobs(
            db,
            q,
            skip=skip,
            limit=limit,
        )
        return JobListResponse(
            total=total,
            page=skip // limit + 1,
            page_size=limit,
            jobs=[JobResponse.from_orm(job) for job in jobs],
        )
    except Exception as e:
        logger.error(f"Error searching jobs: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to search jobs",
        )
