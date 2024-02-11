"""
Google Sheet API interface.
"""

from typing import Optional, List, Any

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


    def get_values(self, range: str) -> Optional[List[Any]]:
        """
        Get values from the spreadsheet.
        """
        try:
            result = (
                self.sheet.values()
                .get(
                    spreadsheetId=self.spreadsheet_id,
                    range=range
                )
                .execute()
            )
            return result.get("values", [])

        except HttpError as err:
            print(err)


    def write_values(
        self, range: str, values: List[Any], value_input_option: Optional[str] = "USER_ENTERED"
    ) -> dict[Any, Any]:
        """
        Write values to the spreadsheet.
        """
        _values = [values]
        _body = {"values": _values}
        try:
            result = (
                self.sheet.values()
                .update(
                    spreadsheetId=self.spreadsheet_id,
                    valueInputOption=value_input_option,
                    body=_body,
                    range=range,
                )
                .execute()
            )
            return result

        except HttpError as err:
            print(err)


    def write_values_batch(
        self, ranges: List[Any], values: List[List[Any]], value_input_option: Optional[str] = "USER_ENTERED"
    ) -> dict[Any, Any]:
        """
        Write discontinues batches of values to the spreadsheet.
        """
        _data = [{"range": _range, "values": [_values]} for (_range, _values) in zip(ranges, values)]
        _body = {"valueInputOption": value_input_option, "data": _data}
        try:
            result = (
                self.sheet.values()
                .batchUpdate(
                    spreadsheetId=self.spreadsheet_id,
                    body=_body
                )
                .execute()
            )
            return result

        except HttpError as err:
            print(err)