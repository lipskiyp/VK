import asyncio

from configs import vk_config
from vk.schemas.stats import VKStatsGetRequest
from vk.interface import VK
from vk.mappers import VKStatsResponseMapper

from sheets import GoogleSheet


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ""
SAMPLE_RANGE_NAME = "Паблик!B17:B"


#group_id=224242420
group_id=207959605
user_id=844300776
app_id=51832179


async def main():
    vk = VK(
        user_token=vk_config.VK_USER_TOKEN,
        group_token=vk_config.VK_GROUP_TOKEN
    )

    res = await vk.stats.get_stats(request=VKStatsGetRequest(
        group_id=group_id,
        timestamp_from=1643730017,
        timestamp_to=1643902817,
        interval="day"
    ))

    ss = VKStatsResponseMapper.vk_stats_to_ss(res)

    sheet = GoogleSheet(spreadsheet_id=SAMPLE_SPREADSHEET_ID)
    all_dates = sheet.get_values(range=SAMPLE_RANGE_NAME)

    print(all_dates)


if __name__ == "__main__":
    asyncio.run(main())
