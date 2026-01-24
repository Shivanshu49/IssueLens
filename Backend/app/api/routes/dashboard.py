from fastapi import APIRouter

from app.schemas.dashboard import DashboardStats, DashboardSummary, RecentActivity

router = APIRouter()


@router.get("/summary", response_model=DashboardSummary)
async def get_dashboard_summary():
    """Get dashboard summary with bug statistics."""
    return {
        "bugs_fixed": 128,
        "open_bugs": 42,
        "regressions": 3,
    }


@router.get("/stats", response_model=DashboardStats)
async def get_dashboard_stats():
    """Get dashboard statistics."""
    # TODO: Aggregate stats from database
    return {
        "total_issues": 0,
        "total_commits": 0,
        "total_explanations": 0,
        "monitored_repos": 0,
    }


@router.get("/activity", response_model=RecentActivity)
async def get_recent_activity():
    """Get recent activity feed."""
    # TODO: Fetch recent events from database
    return {
        "events": [],
    }


@router.get("/repos")
async def get_monitored_repos():
    """Get list of monitored repositories."""
    # TODO: Return list of repos being tracked
    return []


@router.post("/repos")
async def add_monitored_repo(repo_url: str):
    """Add a repository to monitor."""
    # TODO: Validate repo URL
    # TODO: Setup webhook for repo
    # TODO: Store in database
    return {"status": "added", "repo": repo_url}
