from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class GitHubUser(BaseModel):
    login: str
    id: int
    avatar_url: Optional[str] = None


class GitHubRepository(BaseModel):
    id: int
    name: str
    full_name: str
    owner: GitHubUser
    private: bool = False
    html_url: str


class GitHubCommit(BaseModel):
    id: str
    message: str
    author: Dict[str, Any]
    url: str
    added: List[str] = []
    removed: List[str] = []
    modified: List[str] = []


class GitHubWebhookPayload(BaseModel):
    action: Optional[str] = None
    repository: GitHubRepository
    sender: GitHubUser


class PushWebhookPayload(GitHubWebhookPayload):
    ref: str
    before: str
    after: str
    commits: List[GitHubCommit] = []
    head_commit: Optional[GitHubCommit] = None


class IssueWebhookPayload(GitHubWebhookPayload):
    action: str
    issue: Dict[str, Any]


class PullRequestWebhookPayload(GitHubWebhookPayload):
    action: str
    number: int
    pull_request: Dict[str, Any]
