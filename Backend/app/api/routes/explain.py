from fastapi import APIRouter

from app.schemas.issue import ExplainRequest, ExplainResponseSimple

router = APIRouter()


@router.post("", response_model=ExplainResponseSimple)
async def explain_commit(request: ExplainRequest):
    return {
        "explanation": "This change fixes a memory leak caused by improper cleanup."
    }
