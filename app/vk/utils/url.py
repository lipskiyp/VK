"""
Utility class for url operations.
"""

class URL:
    """
    Utility class for url operations
    """
    @staticmethod
    def kwargs_to_query_params(url: str, **kwargs: dict[str, str]):
        """
        Appends kwargs to url as query params.
        """
        for key, arg in kwargs.items():
            url += f"&{key}={arg}"
        return url
