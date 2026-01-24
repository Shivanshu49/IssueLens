from datetime import datetime
from typing import Optional, List

# SQLAlchemy model placeholder - uncomment when adding database
# from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
# from sqlalchemy.orm import relationship
# from app.db.base import Base


class Commit:
    """Commit model for tracking GitHub commits."""
    
    # SQLAlchemy version:
    # __tablename__ = "commits"
    # 
    # id = Column(Integer, primary_key=True, index=True)
    # sha = Column(String(40), unique=True, index=True)
    # repo_owner = Column(String(255), nullable=False)
    # repo_name = Column(String(255), nullable=False)
    # message = Column(Text, nullable=False)
    # author = Column(String(255), nullable=True)
    # diff_content = Column(Text, nullable=True)
    # is_bug_fix = Column(Boolean, default=False)
    # created_at = Column(DateTime, default=datetime.utcnow)
    # 
    # issue_id = Column(Integer, ForeignKey("issues.id"), nullable=True)
    # issue = relationship("Issue", back_populates="commits")
    
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
