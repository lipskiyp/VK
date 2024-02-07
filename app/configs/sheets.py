"""
Google Sheets API base configuration settings
"""

from dotenv import load_dotenv
from os import environ
from pydantic_settings import BaseSettings
from typing import List


load_dotenv("app/.envs/.sheets")


class GoogleSheetConfig(BaseSettings):
    """
    Google Sheets API base configuration settings.
    """
    GOOGLE_TOKEN_PATH: str = environ.get("GOOGLE_TOKEN_PATH")
    GOOGLE_CREDENTIALS_PATH: str = environ.get("GOOGLE_CREDENTIALS_PATH")
    GOOGLE_SCOPES: str = environ.get("GOOGLE_SCOPES")


sheets_config = GoogleSheetConfig()
