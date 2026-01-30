from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class DashboardSummary(BaseModel):
    bugs_fixed: int
    open_bugs: int
    regressions: int


class DashboardStats(BaseModel):
    total_issues: int = 0
    total_commits: int = 0
    total_explanations: int = 0
    monitored_repos: int = 0


class ActivityEvent(BaseModel):
    event_type: str
    timestamp: datetime
    repo: str
    description: str
    metadata: Optional[dict] = None


class RecentActivity(BaseModel):
    events: List[ActivityEvent] = []


class MonitoredRepo(BaseModel):
    id: str
    owner: str
    name: str
    full_name: str
    webhook_active: bool = False
    issues_count: int = 0
    commits_count: int = 0
    last_activity: Optional[datetime] = None
