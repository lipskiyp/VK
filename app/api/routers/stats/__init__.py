from fastapi import APIRouter

from .stats import router as _stats_router


stats_router = APIRouter
stats_router.include_router(_stats_router, prefix="/")


__all__ = [
    "stats_router"
]
