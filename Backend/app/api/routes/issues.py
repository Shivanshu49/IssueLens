from typing import List, Optional
from fastapi import APIRouter, Query

from app.schemas.issue import IssueResponse, IssueWithExplanation, ExplainRequest, ExplainResponseSimple

router = APIRouter()


@router.get("", response_model=List[IssueResponse])
async def get_issues(
    repo: Optional[str] = Query(None, description="Filter by repository"),
    status: Optional[str] = Query(None, description="Filter by status"),
    limit: int = Query(50, le=100),
    offset: int = Query(0, ge=0),
):
    return []


@router.get("/{issue_id}", response_model=IssueWithExplanation)
async def get_issue(issue_id: str):
    return {
        "id": issue_id,
        "title": "Sample Issue",
        "status": "open",
        "explanation": None,
    }


@router.get("/{issue_id}/commits")
async def get_issue_commits(issue_id: str):
    return []


@router.post("/{issue_id}/explain")
async def generate_explanation(issue_id: str):
    return {"status": "processing", "issue_id": issue_id}


@router.post("/explain", response_model=ExplainResponseSimple)
async def explain_commit(request: ExplainRequest):
    return {
        "explanation": "This change fixes a memory leak caused by improper cleanup."
    }
