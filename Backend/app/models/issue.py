from datetime import datetime
from typing import Optional


class Issue:
    def __init__(
        self,
        github_id: int,
        repo_owner: str,
        repo_name: str,
        issue_number: int,
        title: str,
        body: Optional[str] = None,
        status: str = "open",
    ):
        self.github_id = github_id
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.issue_number = issue_number
        self.title = title
        self.body = body
        self.status = status
        self.created_at = datetime.utcnow()
        self.updated_at = None
        self.closed_at = None
