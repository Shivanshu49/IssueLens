"""Pathway schemas for GitHub events."""

from dataclasses import dataclass
from typing import Optional, List

# TODO: Uncomment when pathway is installed
# import pathway as pw


@dataclass
class CommitEvent:
    """Schema for commit events in Pathway."""
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
    """Schema for issue events in Pathway."""
    issue_id: int
    repo_owner: str
    repo_name: str
    issue_number: int
    title: str
    body: Optional[str] = None
    state: str = "open"
    action: str = "opened"
    labels: str = ""  # JSON string of labels


@dataclass
class ExplanationResult:
    """Schema for AI explanation results."""
    commit_sha: str
    summary: str
    what_changed: str  # JSON string
    why_it_fixes: Optional[str] = None
    confidence: float = 0.0


# TODO: Define Pathway schemas
# class CommitEventSchema(pw.Schema):
#     sha: str
#     repo_owner: str
#     repo_name: str
#     message: str
#     author: str
#     timestamp: str
#     files_modified: int
#     additions: int
#     deletions: int
#     is_bug_fix: bool

# class IssueEventSchema(pw.Schema):
#     issue_id: int
#     repo_owner: str
#     repo_name: str
#     issue_number: int
#     title: str
#     body: str
#     state: str
#     action: str
#     labels: str
