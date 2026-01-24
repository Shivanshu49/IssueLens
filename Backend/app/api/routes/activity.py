from typing import List
from fastapi import APIRouter
from pydantic import BaseModel


class ActivityEvent(BaseModel):
    """Activity event schema."""
    type: str
    repo: str
    message: str
    status: str


router = APIRouter()

# In-memory activity store (resets on restart)
_activity_feed: List[dict] = [
    {
        "type": "push",
        "repo": "example/repo",
        "message": "Fix memory leak",
        "status": "fixed"
    },
    {
        "type": "push",
        "repo": "example/repo",
        "message": "Update dependencies",
        "status": "completed"
    },
    {
        "type": "issue",
        "repo": "example/repo",
        "message": "Bug: Login fails on mobile",
        "status": "open"
    },
]


@router.get("", response_model=List[ActivityEvent])
async def get_activity():
    """Get recent activity feed."""
    return _activity_feed


def add_activity(event: dict):
    """Add a new activity event (called from webhooks)."""
    _activity_feed.insert(0, event)
    # Keep only last 50 events
    if len(_activity_feed) > 50:
        _activity_feed.pop()
