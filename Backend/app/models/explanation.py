from datetime import datetime
from typing import Optional, List, Dict, Any


class Explanation:
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
