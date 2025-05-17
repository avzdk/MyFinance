"""
Health check endpoints.
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.session import get_db
from app.schemas.health import HealthResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health check endpoint",
    description="Returns the health status of the API"
)
async def health(db: Session = Depends(get_db)):
    """
    Health check endpoint that returns the status of the API.
    
    Returns:
        HealthResponse: A JSON object containing the status and version of the API
    """
    db_status = "connected" if db else "disconnected"
    return HealthResponse(
        status="healthy",
        version=settings.PROJECT_VERSION,
        db_status=db_status
    )
