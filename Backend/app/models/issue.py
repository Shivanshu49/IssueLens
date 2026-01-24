from datetime import datetime
from typing import Optional

# SQLAlchemy model placeholder - uncomment when adding database
# from sqlalchemy import Column, Integer, String, DateTime, Text
# from app.db.base import Base


class Issue:
    """Issue model for tracking GitHub issues."""
    
    # SQLAlchemy version:
    # __tablename__ = "issues"
    # 
    # id = Column(Integer, primary_key=True, index=True)
    # github_id = Column(Integer, unique=True, index=True)
    # repo_owner = Column(String(255), nullable=False)
    # repo_name = Column(String(255), nullable=False)
    # issue_number = Column(Integer, nullable=False)
    # title = Column(String(500), nullable=False)
    # body = Column(Text, nullable=True)
    # status = Column(String(50), default="open")
    # created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at = Column(DateTime, onupdate=datetime.utcnow)
    # closed_at = Column(DateTime, nullable=True)
    
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
