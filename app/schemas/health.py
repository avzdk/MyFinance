"""
Health-related schemas.
"""
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""
    
    status: str
    version: str
    db_status: str
