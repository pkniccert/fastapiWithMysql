from fastapi import FastAPI

app = FastAPI()

# Import routes
from app.api import main_router

app.include_router(main_router.router, prefix="/api/v1")