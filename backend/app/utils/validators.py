"""Validation utility functions"""
from decimal import Decimal
from typing import List, Optional


def validate_budget(budget_min: float, budget_max: float) -> bool:
    """
    Validate that budget_min <= budget_max
    
    Args:
        budget_min: Minimum budget
        budget_max: Maximum budget
        
    Returns:
        True if valid, False otherwise
    """
    return budget_min <= budget_max and budget_min > 0 and budget_max > 0


def validate_rating(rating: int) -> bool:
    """
    Validate that rating is between 1 and 5
    
    Args:
        rating: Rating value
        
    Returns:
        True if valid, False otherwise
    """
    return 1 <= rating <= 5


def validate_skills(skills: Optional[List[str]]) -> bool:
    """
    Validate skills list
    
    Args:
        skills: List of skills
        
    Returns:
        True if valid, False otherwise
    """
    if skills is None:
        return True
    return len(skills) > 0 and all(isinstance(skill, str) and len(skill) > 0 for skill in skills)


def validate_phone(phone: Optional[str]) -> bool:
    """
    Basic phone validation
    
    Args:
        phone: Phone number
        
    Returns:
        True if valid, False otherwise
    """
    if phone is None:
        return True
    # Remove common separators
    cleaned = "".join(c for c in phone if c.isdigit())
    return len(cleaned) >= 7 and len(cleaned) <= 15
