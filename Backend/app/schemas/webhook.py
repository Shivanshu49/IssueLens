from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class GitHubUser(BaseModel):
    """GitHub user schema."""
    login: str
    id: int
    avatar_url: Optional[str] = None


class GitHubRepository(BaseModel):
    """GitHub repository schema."""
    id: int
    name: str
    full_name: str
    owner: GitHubUser
    private: bool = False
    html_url: str


class GitHubCommit(BaseModel):
    """GitHub commit in webhook payload."""
    id: str
    message: str
    author: Dict[str, Any]
    url: str
    added: List[str] = []
    removed: List[str] = []
    modified: List[str] = []


class GitHubWebhookPayload(BaseModel):
    """Base GitHub webhook payload."""
    action: Optional[str] = None
    repository: GitHubRepository
    sender: GitHubUser


class PushWebhookPayload(GitHubWebhookPayload):
    """Push event webhook payload."""
    ref: str
    before: str
    after: str
    commits: List[GitHubCommit] = []
    head_commit: Optional[GitHubCommit] = None


class IssueWebhookPayload(GitHubWebhookPayload):
    """Issue event webhook payload."""
    action: str
    issue: Dict[str, Any]


class PullRequestWebhookPayload(GitHubWebhookPayload):
    """Pull request event webhook payload."""
    action: str
    number: int
    pull_request: Dict[str, Any]
