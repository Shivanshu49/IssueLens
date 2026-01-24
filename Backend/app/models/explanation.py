from datetime import datetime
from typing import Optional, List, Dict, Any

# SQLAlchemy model placeholder - uncomment when adding database
# from sqlalchemy import Column, Integer, String, DateTime, Text, Float, ForeignKey, JSON
# from sqlalchemy.orm import relationship
# from app.db.base import Base


class Explanation:
    """Explanation model for AI-generated bug fix explanations."""
    
    # SQLAlchemy version:
    # __tablename__ = "explanations"
    # 
    # id = Column(Integer, primary_key=True, index=True)
    # commit_sha = Column(String(40), ForeignKey("commits.sha"), nullable=False)
    # summary = Column(Text, nullable=False)
    # what_changed = Column(JSON, nullable=True)
    # why_it_fixes = Column(Text, nullable=True)
    # potential_impact = Column(Text, nullable=True)
    # confidence = Column(Float, default=0.0)
    # model_used = Column(String(100), nullable=True)
    # created_at = Column(DateTime, default=datetime.utcnow)
    # 
    # commit = relationship("Commit", back_populates="explanations")
    
    def __init__(
        self,
        commit_sha: str,
        summary: str,
        what_changed: Optional[List[str]] = None,
        why_it_fixes: Optional[str] = None,
        potential_impact: Optional[str] = None,
        confidence: float = 0.0,
        model_used: Optional[str] = None,
    ):
        self.commit_sha = commit_sha
        self.summary = summary
        self.what_changed = what_changed or []
        self.why_it_fixes = why_it_fixes
        self.potential_impact = potential_impact
        self.confidence = confidence
        self.model_used = model_used
        self.created_at = datetime.utcnow()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "commit_sha": self.commit_sha,
            "summary": self.summary,
            "what_changed": self.what_changed,
            "why_it_fixes": self.why_it_fixes,
            "potential_impact": self.potential_impact,
            "confidence": self.confidence,
            "model_used": self.model_used,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
