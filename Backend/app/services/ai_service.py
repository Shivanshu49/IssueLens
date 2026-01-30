from typing import Dict, Any, Optional
import httpx

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class AIService:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        self.model = settings.AI_MODEL
    
    async def explain_bug_fix(
        self,
        diff_content: str,
        commit_message: str,
        issue_context: Optional[str] = None,
    ) -> Dict[str, Any]:
        prompt = self._build_explanation_prompt(diff_content, commit_message, issue_context)
        
        return {
            "summary": "Bug fix explanation pending implementation",
            "what_changed": [],
            "why_it_fixes": "",
            "potential_impact": "",
            "confidence": 0.0,
        }
    
    def _build_explanation_prompt(
        self,
        diff_content: str,
        commit_message: str,
        issue_context: Optional[str] = None,
    ) -> str:
        prompt = f"""Analyze this code change and explain the bug fix:

Commit Message: {commit_message}

Code Diff:
```
{diff_content[:4000]}
```
"""
        
        if issue_context:
            prompt += f"\nRelated Issue Context:\n{issue_context}\n"
        
        prompt += """
Please provide:
1. A brief summary of what was changed
2. What bug this fixes and why
3. Potential impact of this change
"""
        return prompt
    
    async def summarize_pr(self, diff_content: str, pr_title: str) -> Dict[str, Any]:
        return {
            "summary": "PR summary pending implementation",
            "key_changes": [],
        }


ai_service = AIService()
