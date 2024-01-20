"""
Main developer interface to interact with VK API.
"""

from typing import Optional

from .auth import Auth
from .stats import Stats


class VK:
    """
    Main developer interface to interact with VK API.
    """

    def __init__(
        self, user_token: Optional[str] = None, group_token: Optional[str] = None
    ):
        self.user_token = user_token
        self.group_token = group_token

    @property
    def auth(self) -> Auth:
        """
        Returns VK API authorization interface.
        """
        return Auth(
            self.user_token, self.group_token
        )

    @property
    def stats(self) -> Stats:
        """
        Returns VK API stats interface.
        """
        return Stats(
            self.user_token, self.group_token
        )
