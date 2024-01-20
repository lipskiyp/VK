"""
Interface for http requests.
"""

from httpx import AsyncClient


class Request:
    """
    HTTP requests interface.
    """

    @classmethod
    async def get(cls, url: str, **kwargs):
        """
        Makes async GET http request and returns response.
        """
        async with AsyncClient() as client:
            return await client.get(url=url, **kwargs)


    @classmethod
    async def post(cls, url: str, headers: dict[str, str], data: dict[str, str], **kwargs):
        """
        Makes async POST http request and returns response.
        """
        async with AsyncClient() as client:
            return await client.post(url=url, headers=headers, data=data, **kwargs)
