"""
Base model classes for SQLAlchemy models.
"""
from sqlalchemy import Column, Integer, DateTime, func
from app.database.session import Base


class BaseModel(object):
    """Base model with common fields."""
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
