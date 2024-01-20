"""
VK API base configuration settings
"""

from dotenv import load_dotenv
from os import environ
from pydantic_settings import BaseSettings


load_dotenv("app/.envs/.vk")


class VKConfig(BaseSettings):
    """
    VK API base configuration settings.
    """

    VK_GROUP_TOKEN: str = environ.get("VK_GROUP_TOKEN")
    VK_USER_TOKEN: str = environ.get("VK_USER_TOKEN")

    VK_APP_SECURE_KEY: str = environ.get("VK_APP_SECURE_KEY")
    VK_APP_SERVICE_KEY: str = environ.get("VK_APP_SERVICE_KEY")

    VK_API_VERSION: str = environ.get("VK_API_VERSION", "5.199")

    VK_API_BASE_URL: str = environ.get("VK_API_BASE_URL", "https://api.vk.com/method")
    VK_API_AUTH_URL: str = environ.get("VK_API_AUTH_URL", "https://oauth.vk.com")
    VK_API_AUTH_REDIRECT_URL: str = environ.get("VK_API_AUTH_REDIRECT_URL", "https://oauth.vk.com/blank.html")


config = VKConfig()
