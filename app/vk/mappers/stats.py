"""
VK Group Stats response mappers.
"""

from typing import Any

from vk.utils import DatesUtil
import vk.schemas.stats as schemas


class VKStatsResponseMapper:
    """
    Maps VK stats responses.
    """

    @classmethod
    def vk_stats_to_ss(
        cls, response: schemas.VKStatsGetResponse
    ) -> dict[str, Any]:
        """
        Map VKStatsGetResponse to spreadsheet format.
        """
        res = {}  # results hashed by date
        for period in response.response:
            period_from = DatesUtil.timestamp_to_ssdate(period.period_from)
            reach_sub = period.reach.reach_subscribers
            reach_vir = period.reach.reach
            posts_count = None  # TO DO
            visitors = period.visitors.visitors
            subscribed = period.activity.subscribed
            unsubscribed = period.activity.unsubscribed
            copies = period.activity.copies  # Рассказали друзьям
            comments = period.activity.comments
            likes = period.activity.likes

            values = [
                reach_sub,  # Reach sub
                reach_vir,  # Reach vir
                "",
                posts_count,  # Количество постов
                visitors,  # Visitors
                subscribed,  # Новые участники
                unsubscribed,  # Вышедшие участники
                copies,  # Рассказали друзьям
                comments,  # Комментарии
                likes,  # Нравится
            ]

            res[period_from] = values

        return res
