import asyncio
from datetime import datetime
from time import mktime

from configs import vk_config
from sheets import GoogleSheet
from vk.interface import VK
from vk.mappers import VKStatsResponseMapper
from vk.schemas.stats import VKStatsGetRequest


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ""
DATES_RANGE = "Паблик!B:B"


group_id=207959605
user_id=844300776
app_id=51832179


async def main():
    # Initiate VK API inreface
    vk = VK(
        user_token=vk_config.VK_USER_TOKEN,
        group_token=vk_config.VK_GROUP_TOKEN
    )

    # Initiate Google Sheets API interface
    sheet = GoogleSheet(spreadsheet_id=SAMPLE_SPREADSHEET_ID)

    # Collect stats data from VK
    _stats = await vk.stats.get_stats(request=VKStatsGetRequest(
        group_id=group_id,
        timestamp_from=mktime(datetime.fromisoformat("2022-01-02+03:00").timetuple()),  # Will start on previous day
        timestamp_to=mktime(datetime.fromisoformat("2022-02-28+03:00").timetuple()),
        interval="day"
    ))
    stats = VKStatsResponseMapper.vk_stats_to_ss(_stats)

    # Collect all dates in the spreadsheet
    all_dates = sheet.get_values(range=DATES_RANGE)

    # Prepare data for write
    ranges, values = [], []
    for date, row in stats.items():
        if [date] in all_dates:
            i = all_dates.index([date]) + 1  # NB sheet rows start with 1
            ranges.append(f"Паблик!C{i}:L{i}")
            values.append(row)

    # Write data to spreadsheet
    sheet.write_values_batch(
        ranges=ranges,
        values=values
    )

if __name__ == "__main__":
    asyncio.run(main())
