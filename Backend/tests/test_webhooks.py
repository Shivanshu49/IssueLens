import pytest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


class TestHealthEndpoints:
    """Test health check endpoints."""
    
    def test_health_check(self):
        response = client.get("/api/v1/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
    
    def test_readiness_check(self):
        response = client.get("/api/v1/health/ready")
        assert response.status_code == 200
        assert response.json()["status"] == "ready"


class TestWebhookEndpoints:
    """Test GitHub webhook endpoints."""
    
    def test_push_webhook(self):
        payload = {
            "ref": "refs/heads/main",
            "before": "abc123",
            "after": "def456",
            "repository": {
                "id": 123,
                "name": "test-repo",
                "full_name": "owner/test-repo",
                "owner": {
                    "login": "owner",
                    "id": 1,
                },
                "private": False,
                "html_url": "https://github.com/owner/test-repo",
            },
            "sender": {
                "login": "developer",
                "id": 2,
            },
            "commits": [
                {
                    "id": "def456",
                    "message": "Fix bug in authentication",
                    "author": {"name": "Developer", "email": "dev@example.com"},
                    "url": "https://github.com/owner/test-repo/commit/def456",
                    "added": [],
                    "removed": [],
                    "modified": ["src/auth.py"],
                }
            ],
        }
        
        response = client.post(
            "/api/v1/webhooks/github",
            json=payload,
            headers={"X-GitHub-Event": "push"},
        )
        
        assert response.status_code == 200
        assert response.json()["status"] == "received"
        assert response.json()["event"] == "push"
    
    def test_issue_webhook(self):
        payload = {
            "action": "opened",
            "issue": {
                "number": 42,
                "title": "Bug: Login fails",
                "body": "Cannot login with valid credentials",
                "state": "open",
                "labels": [{"name": "bug"}],
            },
            "repository": {
                "id": 123,
                "name": "test-repo",
                "full_name": "owner/test-repo",
                "owner": {"login": "owner", "id": 1},
                "private": False,
                "html_url": "https://github.com/owner/test-repo",
            },
            "sender": {"login": "reporter", "id": 3},
        }
        
        response = client.post(
            "/api/v1/webhooks/github",
            json=payload,
            headers={"X-GitHub-Event": "issues"},
        )
        
        assert response.status_code == 200
        assert response.json()["event"] == "issues"


class TestIssueEndpoints:
    """Test issue endpoints."""
    
    def test_get_issues(self):
        response = client.get("/api/v1/issues")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_get_issue(self):
        response = client.get("/api/v1/issues/test-123")
        assert response.status_code == 200
        assert "id" in response.json()


class TestDashboardEndpoints:
    """Test dashboard endpoints."""
    
    def test_get_stats(self):
        response = client.get("/api/v1/dashboard/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_issues" in data
        assert "total_commits" in data
    
    def test_get_activity(self):
        response = client.get("/api/v1/dashboard/activity")
        assert response.status_code == 200
        assert "events" in response.json()
