from typing import Optional, List, Dict, Any
import httpx

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class GitHubService:
    BASE_URL = "https://api.github.com"
    
    def __init__(self):
        self.headers = {
            "Authorization": f"token {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }
    
    async def get_commit(self, owner: str, repo: str, sha: str) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/commits/{sha}",
                headers=self.headers,
            )
            response.raise_for_status()
            return response.json()
    
    async def get_commit_diff(self, owner: str, repo: str, sha: str) -> str:
        headers = {**self.headers, "Accept": "application/vnd.github.v3.diff"}
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/commits/{sha}",
                headers=headers,
            )
            response.raise_for_status()
            return response.text
    
    async def get_issue(self, owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}",
                headers=self.headers,
            )
            response.raise_for_status()
            return response.json()
    
    async def get_pull_request(self, owner: str, repo: str, pr_number: int) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}",
                headers=self.headers,
            )
            response.raise_for_status()
            return response.json()
    
    async def get_pr_diff(self, owner: str, repo: str, pr_number: int) -> str:
        headers = {**self.headers, "Accept": "application/vnd.github.v3.diff"}
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}",
                headers=headers,
            )
            response.raise_for_status()
            return response.text


github_service = GitHubService()
