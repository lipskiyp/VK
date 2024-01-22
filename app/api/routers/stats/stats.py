"""
FastAPI endpoints for VK.Stats
"""

from fastapi import APIRouter, Depends


router = APIRouter()


@router.get(
    "/",
    summary="test"
)
async def ping():
    return "Pong"
