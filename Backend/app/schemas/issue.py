from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class IssueBase(BaseModel):
    """Base issue schema."""
    title: str
    body: Optional[str] = None
    status: str = "open"


class IssueCreate(IssueBase):
    """Schema for creating an issue."""
    github_id: int
    repo_owner: str
    repo_name: str
    issue_number: int


class IssueResponse(IssueBase):
    """Schema for issue response."""
    id: str
    github_id: Optional[int] = None
    repo_owner: Optional[str] = None
    repo_name: Optional[str] = None
    issue_number: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ExplanationResponse(BaseModel):
    """Schema for explanation response."""
    summary: str
    what_changed: List[str] = []
    why_it_fixes: Optional[str] = None
    potential_impact: Optional[str] = None
    confidence: float = 0.0


class IssueWithExplanation(IssueResponse):
    """Issue with AI-generated explanation."""
    explanation: Optional[ExplanationResponse] = None
    related_commits: List[str] = []


class ExplainRequest(BaseModel):
    """Request schema for AI explanation."""
    commit_message: str


class ExplainResponseSimple(BaseModel):
    """Response schema for AI explanation."""
    explanation: str
