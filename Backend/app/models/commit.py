from datetime import datetime
from typing import Optional, List


class Commit:
    def __init__(
        self,
        sha: str,
        repo_owner: str,
        repo_name: str,
        message: str,
        author: Optional[str] = None,
        diff_content: Optional[str] = None,
        is_bug_fix: bool = False,
        related_issues: Optional[List[int]] = None,
    ):
        self.sha = sha
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.message = message
        self.author = author
        self.diff_content = diff_content
        self.is_bug_fix = is_bug_fix
        self.related_issues = related_issues or []
        self.created_at = datetime.utcnow()
