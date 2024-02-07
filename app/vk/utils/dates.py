"""
Util function for date conversions.
"""

from datetime import datetime
from time import time


class DatesUtil:

    @classmethod
    def timestamp_to_ssdate(
        cls, timestamp: time
    ) -> str:
        """
        Converts timestamp to spreadsheet date.
        """
        date = datetime.fromtimestamp(timestamp)
        day = str(date.day).zfill(2)
        month = str(date.month).zfill(2)
        year = str(date.year)
        return f"{day}.{month}.{year}"
