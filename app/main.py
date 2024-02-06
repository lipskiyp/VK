import asyncio

from vk.config import config
from vk.schemas.stats import VKStatsGetRequest, VKStatsGetResponse
from vk.interface import VK
from vk.mappers import VKStatsResponseMapper


#group_id=224242420
group_id=207959605
user_id=844300776
app_id=51832179


async def main():
    vk = VK(
        user_token=config.VK_USER_TOKEN,
        group_token=config.VK_GROUP_TOKEN
    )


    res = await vk.stats.get_stats(request=VKStatsGetRequest(
        group_id=group_id,
        timestamp_from=1643730017,
        timestamp_to=1643902817,
        interval="day"
    ))

    ss = VKStatsResponseMapper.vk_stats_to_ss(res)


if __name__ == "__main__":
    asyncio.run(main())
