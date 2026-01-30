from fastapi import APIRouter, Request, BackgroundTasks, Depends
from app.schemas.webhook import GitHubWebhookPayload
from app.services.github_service import GitHubService
from app.services.diff_service import DiffService
from app.services.ai_service import AIService
from app.core.security import verify_github_signature
from app.core.logging import get_logger

router = APIRouter()
logger = get_logger(__name__)


@router.post("/github")
async def handle_github_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
):
    
    event_type = request.headers.get("X-GitHub-Event", "unknown")
    payload = await request.json()
    
    logger.info(f"Received GitHub webhook: {event_type}")
    
    if event_type == "push":
        background_tasks.add_task(process_push_event, payload)
    elif event_type == "issues":
        background_tasks.add_task(process_issue_event, payload)
    elif event_type == "pull_request":
        background_tasks.add_task(process_pr_event, payload)
    
    return {"status": "received", "event": event_type}


async def process_push_event(payload: dict):
    logger.info(f"Processing push event for repo: {payload.get('repository', {}).get('full_name')}")


async def process_issue_event(payload: dict):
    logger.info(f"Processing issue event: {payload.get('action')}")


async def process_pr_event(payload: dict):
    logger.info(f"Processing PR event: {payload.get('action')}")
