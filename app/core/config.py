"""
Application settings and configuration.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    PROJECT_NAME: str = "MyFinance API"
    PROJECT_DESCRIPTION: str = "A FastAPI backend for financial management"
    PROJECT_VERSION: str = "0.1.0"
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./myfinance.db"
    
    class Config:
        """Pydantic config."""
        case_sensitive = True
        env_file = ".env"


# Create settings instance
settings = Settings()
