"""
Google API authentication module.
"""

import os.path
from typing import Optional, List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow

from configs import sheets_config


class GoogleAuth:
    def __init__(
        self,
        scopes: List[str] = [sheets_config.GOOGLE_SCOPES],
        token_path: Optional[str] = sheets_config.GOOGLE_TOKEN_PATH,
        credentials_path: Optional[str] = sheets_config.GOOGLE_CREDENTIALS_PATH
    ):
        """
        GoogleSheets API Interface.
        """
        self.scopes = scopes
        self.token_path = token_path
        self.credentials_path = credentials_path
        self.creds = None
        self.init_authorization()


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
