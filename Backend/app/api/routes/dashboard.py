from fastapi import APIRouter

from app.schemas.dashboard import DashboardStats, DashboardSummary, RecentActivity

from fastapi import APIRouter, Depends
from app.api import deps
from app.models.user import User
from app.schemas.dashboard import DashboardStats, DashboardSummary, RecentActivity

router = APIRouter()


@router.get("/summary", response_model=DashboardSummary)
async def get_dashboard_summary(
    current_user: User = Depends(deps.get_current_user),
):
    return {
        "bugs_fixed": 128,
        "open_bugs": 42,
        "regressions": 3,
    }


@router.get("/stats", response_model=DashboardStats)
async def get_dashboard_stats(
    current_user: User = Depends(deps.get_current_user),
):
    return {
        "total_issues": 0,
        "total_commits": 0,
        "total_explanations": 0,
        "monitored_repos": 0,
    }


@router.get("/activity", response_model=RecentActivity)
async def get_recent_activity(
    current_user: User = Depends(deps.get_current_user),
):
    return {
        "events": [],
    }


@router.get("/repos")
async def get_monitored_repos(
    current_user: User = Depends(deps.get_current_user),
):
    return []


@router.post("/repos")
async def add_monitored_repo(
    repo_url: str,
    current_user: User = Depends(deps.get_current_user),
):
    return {"status": "added", "repo": repo_url}
