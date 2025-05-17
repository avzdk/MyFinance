from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(
    title="MyFinance API",
    description="A FastAPI backend for financial management",
    version="0.1.0"
)

class HealthResponse(BaseModel):
    status: str
    version: str


@app.get(
    "/health", 
    response_model=HealthResponse, 
    status_code=status.HTTP_200_OK,
    summary="Health check endpoint",
    description="Returns the health status of the API"
)
async def health():
    """
    Health check endpoint that returns the status of the API.
    
    Returns:
        HealthResponse: A JSON object containing the status and version of the API
    """
    return HealthResponse(status="healthy", version="0.1.0")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
