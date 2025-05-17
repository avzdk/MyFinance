from fastapi import FastAPI, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MyFinance API",
    description="A FastAPI backend for financial management",
    version="0.1.0"
)

class HealthResponse(BaseModel):
    status: str
    version: str
    db_status: str


@app.get(
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
    return HealthResponse(status="healthy", version="0.1.0", db_status=db_status)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
