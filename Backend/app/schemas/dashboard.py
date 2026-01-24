from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class DashboardSummary(BaseModel):
    """Dashboard summary schema."""
    bugs_fixed: int
    open_bugs: int
    regressions: int


class DashboardStats(BaseModel):
    """Dashboard statistics schema."""
    total_issues: int = 0
    total_commits: int = 0
    total_explanations: int = 0
    monitored_repos: int = 0


class ActivityEvent(BaseModel):
    """Single activity event."""
    event_type: str
    timestamp: datetime
    repo: str
    description: str
    metadata: Optional[dict] = None


class RecentActivity(BaseModel):
    """Recent activity feed."""
    events: List[ActivityEvent] = []


class MonitoredRepo(BaseModel):
    """Monitored repository schema."""
    id: str
    owner: str
    name: str
    full_name: str
    webhook_active: bool = False
    issues_count: int = 0
    commits_count: int = 0
    last_activity: Optional[datetime] = None
