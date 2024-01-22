from fastapi import APIRouter

from .stats import stats_router


api_router = APIRouter()
api_router.include_router(stats_router, prefix="/stats")

__all__ = [
    "api_router"
]
