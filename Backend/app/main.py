from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging

# Setup logging
setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Real-time AI platform that monitors GitHub repositories and explains bug fixes",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    # Initialize Database Tables
    from app.db.base import Base, engine
    Base.metadata.create_all(bind=engine)
    
    # TODO: Initialize Pathway pipeline
    # pathway_service.initialize_pipeline()
    pass


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    # TODO: Graceful shutdown of Pathway pipeline
    # TODO: Close database connections
    pass
