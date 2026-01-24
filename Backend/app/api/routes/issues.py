from typing import List, Optional
from fastapi import APIRouter, Query

from app.schemas.issue import IssueResponse, IssueWithExplanation

router = APIRouter()


@router.get("", response_model=List[IssueResponse])
async def get_issues(
    repo: Optional[str] = Query(None, description="Filter by repository"),
    status: Optional[str] = Query(None, description="Filter by status"),
    limit: int = Query(50, le=100),
    offset: int = Query(0, ge=0),
):
    """Get list of tracked issues."""
    # TODO: Query database for issues
    # TODO: Apply filters
    return []


@router.get("/{issue_id}", response_model=IssueWithExplanation)
async def get_issue(issue_id: str):
    """Get a specific issue with AI-generated explanation."""
    # TODO: Fetch issue from database
    # TODO: Include related commits and explanations
    return {
        "id": issue_id,
        "title": "Sample Issue",
        "status": "open",
        "explanation": None,
    }


@router.get("/{issue_id}/commits")
async def get_issue_commits(issue_id: str):
    """Get commits related to an issue."""
    # TODO: Find commits that reference this issue
    return []


@router.post("/{issue_id}/explain")
async def generate_explanation(issue_id: str):
    """Trigger AI explanation generation for an issue."""
    # TODO: Fetch issue and related diffs
    # TODO: Send to AI service for explanation
    return {"status": "processing", "issue_id": issue_id}
