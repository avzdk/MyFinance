"""
Application initialization module.
"""
from fastapi import FastAPI

from app.core.config import settings
from app.database import Base, engine


def create_tables() -> None:
    """Create database tables."""
    Base.metadata.create_all(bind=engine)


def include_routers(app: FastAPI) -> None:
    """Include all routers in the application."""
    from app.routes.health import router as health_router
    
    app.include_router(health_router)
    # Add other routers here as your application grows


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""
    # Create database tables
    create_tables()
    
    # Initialize FastAPI
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )
    
    # Include routers
    include_routers(app)
    
    return app
