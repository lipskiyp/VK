import asyncio

from vk.config import config
from vk.schemas.stats import VKStatsGetRequest
from vk.interface import VK


group_id=224242420
user_id=844300776
app_id=51832179


async def main():
    vk = VK(
        user_token=config.VK_USER_TOKEN,
        group_token=config.VK_GROUP_TOKEN
    )

    res = await vk.stats.get_stats(request=VKStatsGetRequest(
        group_id=group_id,
        timestamp_from=1705536000
    ))

    print(res)


if __name__ == "__main__":
    asyncio.run(main())
