from dataclasses import dataclass
from typing import Optional, List


@dataclass
class CommitEvent:
    sha: str
    repo_owner: str
    repo_name: str
    message: str
    author: str
    timestamp: str
    files_modified: int = 0
    additions: int = 0
    deletions: int = 0
    is_bug_fix: bool = False


@dataclass
class IssueEvent:
    issue_id: int
    repo_owner: str
    repo_name: str
    issue_number: int
    title: str
    body: Optional[str] = None
    state: str = "open"
    action: str = "opened"
    labels: str = ""


@dataclass
class ExplanationResult:
    commit_sha: str
    summary: str
    what_changed: str
    why_it_fixes: Optional[str] = None
    confidence: float = 0.0
