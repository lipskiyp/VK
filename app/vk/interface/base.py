"""
Base VK API interface.
"""

from abc import ABC
from typing import Optional

from configs import vk_config
from vk._requests import Request


class _Base(ABC):
    """
    Base VK API interface.
    """
    VK_API_VERSION = vk_config.VK_API_VERSION
    VK_API_BASE_URL = vk_config.VK_API_BASE_URL
    VK_API_AUTH_URL = vk_config.VK_API_AUTH_URL
    VK_API_AUTH_REDIRECT_URL = vk_config.VK_API_AUTH_REDIRECT_URL

    def __init__(
        self, user_token: Optional[str] = None, group_token: Optional[str] = None
    ):

        self._USER_HEADERS = {"Authorization": f"Bearer {user_token}"} if user_token else {}
        self._GROUP_HEADERS = {"Authorization": f"Bearer {group_token}"} if group_token else {}

    @classmethod
    def method_url(cls, method: str):
        """
        Returns url for a method.
        """
        return f"{cls.VK_API_BASE_URL}/{method}/?v={cls.VK_API_VERSION}"

    @property
    def USER_HEADERS(self):
        return self._USER_HEADERS

    @USER_HEADERS.setter
    def USER_HEADERS(self, value):
        # TO DO
        pass

    @property
    def GROUP_HEADERS(self):
        return self._GROUP_HEADERS

    @GROUP_HEADERS.setter
    def GROUP_HEADERS(self, value):
        # TO DO
        pass

    @property
    def requests(self) -> Request:
        """
        Returns interface to for HTTP requests.
        """
        return Request()
