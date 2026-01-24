from fastapi import APIRouter

from app.api.routes import webhooks, issues, dashboard, health

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])
api_router.include_router(issues.router, prefix="/issues", tags=["issues"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
