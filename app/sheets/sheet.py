"""
Google Sheet API interface.
"""

from typing import Optional

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .auth import GoogleAuth


class GoogleSheet(GoogleAuth):
    def __init__(
        self,
        spreadsheet_id: Optional[str],
    ):
        super().__init__()
        self.spreadsheet_id = spreadsheet_id


    @property
    def sheet(self):
        """
        Initialise sheet object.
        """
        service = build("sheets", "v4", credentials=self.creds)
        return service.spreadsheets()


    def get_values(self, range: str):
        """
        Get values from spreadsheet
        """
        try:
            result = (
                self.sheet.values()
                .get(spreadsheetId=self.spreadsheet_id, range=range)
                .execute()
            )
            return result.get("values", [])

        except HttpError as err:
            print(err)
