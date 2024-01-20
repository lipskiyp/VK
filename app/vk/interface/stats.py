"""
VK API stats interface.
"""

from typing import Optional

import vk.schemas.stats as schemas
from .base import _Base


class Stats(_Base):
    """
    VK API stats interface.
    """
    statsGet = "stats.get"
    statsGetPostReach = "stats.getPostReach"

    def __init__(
        self, user_token: Optional[str] = None, group_token: Optional[str] = None
    ):
        super().__init__(user_token, group_token)


    async def get_stats(
        self, request: schemas.VKStatsGetRequest
    ) -> Optional[schemas.VKStatsGetResponse]:
        """
        Makes request to VK API and returns VKStatsGetResponse object.

        https://dev.vk.com/ru/method/stats.get
        """
        res = await self.requests.post(
            url = self.method_url(method=self.statsGet),
            data = request.model_dump(exclude_none=True),
            headers = self.USER_HEADERS,
        )

        return schemas.VKStatsGetResponse.model_validate(
            res.json()
        )


    async def get_stats_post_reach(
            self, request: schemas.VKStatsGetPostReachRequest
    ) -> Optional[schemas.VKStatsGetPostReachResponse]:
        """
        Makes request to VK API and returns !!! object.

        https://dev.vk.com/ru/method/stats.getPostReach
        """
        # TO FINISH
        return None
        res = await self.requests.post(
            url = self.method_url(method=self.statsGetPostReach),
            data = request.model_dump(exclude_none=True),
            headers = self.USER_HEADERS,
        )

        return schemas.VKStatsGetPostReachResponse.model_validate(
            res.json()
        )
