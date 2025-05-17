"""
Main entrypoint for the MyFinance API application.
"""
from app.core.app import create_application

# Create the FastAPI application
app = create_application()

# This is used when running locally with `python -m app.main`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
