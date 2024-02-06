"""
VK Group Stats response mappers.
"""

import vk.schemas.stats as schemas


class VKStatsResponseMapper:
    """
    Maps VK stats responses.
    """

    @classmethod
    def vk_stats_to_ss(
        cls, response: schemas.VKStatsGetResponse
    ):
        """
        Map VK
        """
        print(response)
        for period in response.response:
            print(period)
            print()