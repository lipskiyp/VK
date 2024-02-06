import os.path
from typing import Optional, List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ""
SAMPLE_RANGE_NAME = "Паблик!A2:A13"


# TOKEN and CREDENTIALS
TOKEN_PATH = "app/sheets/token.json"
CREDENTIALS_PATH = "app/sheets/credentials.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


class GoogleSheet:
    def __init__(
        self,
        scopes: List[str] = SCOPES,
        spreadsheet_id: Optional[str] = SAMPLE_SPREADSHEET_ID,
        token_path: Optional[str] = TOKEN_PATH,
        credentials_path: Optional[str] = CREDENTIALS_PATH
    ):
        """
        GoogleSheets API Interface.
        """
        self.spreadsheet_id = spreadsheet_id
        self.token_path = token_path
        self.credentials_path = credentials_path

        self.creds = None
        self.sheet = None
        self.scopes = scopes

        self.init_authorization()
        self.init_sheet()


    def init_authorization(self) -> None:
        """
        The file self.token_path stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first time.
        """
        if os.path.exists(self.token_path):
            self.creds = Credentials.from_authorized_user_file(
                self.token_path, self.scopes
            )

        # If no valid creds, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                try:
                    self.creds.refresh(Request())
                except RefreshError:
                    self._installed_app_flow()

            else:
               self._installed_app_flow()

            # Save the credentials for the next run
            with open(self.token_path, "w") as token:
                token.write(self.creds.to_json())


    def _installed_app_flow(self) -> None:
        """
        Initialise InstalledAppFlow to generate new Token.
        """
        flow = InstalledAppFlow.from_client_secrets_file(
            self.credentials_path, self.scopes
        )
        self.creds = flow.run_local_server(port=0)


    def init_sheet(self) -> None:
        """
        Initialise sheet object.
        """
        try:
            service = build("sheets", "v4", credentials=self.creds)
            self.sheet = service.spreadsheets()

        except HttpError as err:
            print(err)


    def get_values(self, range: str):
        """
        Get values from spreadsheet
        """
        result = (
            self.sheet.values()
            .get(spreadsheetId=self.spreadsheet_id, range=range)
            .execute()
        )
        return result.get("values", [])



if __name__ == "__main__":
    sheet = GoogleSheet()
    res = sheet.get_values(range=SAMPLE_RANGE_NAME)
    print(res)
