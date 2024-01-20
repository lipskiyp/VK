"""
Pydantic schemas for VK.Stats.GetPostReach
"""

from pydantic import BaseModel
from typing import Optional, List


class VKStatsGetPostReachRequest(BaseModel):
    """
    Pydantic schema for VK.Stats.Get requests.
    """
    owner_id: int
    post_ids: int


class VKStatsGetPostReachResponse(BaseModel):
    """
    Pydantic schema for VK.Stats.Get response.
    """