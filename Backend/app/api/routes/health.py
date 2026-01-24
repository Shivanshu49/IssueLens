from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def health_check():
    """Basic health check endpoint."""
    return {"status": "healthy", "service": "IssueLens API"}


@router.get("/ready")
async def readiness_check():
    """Readiness check for Kubernetes/Docker."""
    # TODO: Check database connection
    # TODO: Check Pathway pipeline status
    return {"status": "ready"}
