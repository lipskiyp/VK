"""
VK API authorization interface.
"""

from typing import Optional

from vk.utils import URL
from .base import _Base


BASE_SCOPE = "notify,friends,photos,audio,video,stories,pages,menu,status,notes,messages,wall,adds,offline,docs,groups,notifications,stats,email,market,phone_number"


class Auth(_Base):
    """
    VK API authorization interface.
    """
    authorize = "authorize"

    def __init__(
        self, user_token: Optional[str] = None, group_token: Optional[str] = None
    ):
        super().__init__(user_token, group_token)

    def get_user_authorization_url(
        self, app_id: str, response_type: str, scope: Optional[str] = None, **kwargs: dict[str, str]
    ) -> str:
        """
        Returns url for user authentication.

        :param response_type: "token" | "key"
        """
        if not scope: scope = BASE_SCOPE
        _url = f"{self.VK_API_AUTH_URL}/{self.authorize}/?client_id={app_id}&redirect_uri={self.VK_API_AUTH_REDIRECT_URL}&display=page&response_type={response_type}&scope={scope}"
        return URL.kwargs_to_query_params(_url, **kwargs)


    def get_group_authorization_url(
        self, app_id: str, group_ids: str, response_type: str, scope: Optional[str] = None, **kwargs: dict[str, str]
    ) -> str:
        """
        Returns url for group authentication.

        :param response_type: "token" | "key"
        """
        if not scope: scope = BASE_SCOPE
        _url = f"{self.VK_API_AUTH_URL}/{self.authorize}/?client_id={app_id}&group_ids={group_ids}&redirect_uri={self.VK_API_AUTH_REDIRECT_URL}&display=page&response_type={response_type}&scope={scope}"
        return URL.kwargs_to_query_params(_url, **kwargs)
