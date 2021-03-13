secret_key: str = None
api_version: str = "v1"
from .accept import *  # noqa


def api_base_url() -> str:
    """

    :return: str api_next_url
    """
    api_next_url: str = "http://127.0.0.1:49152/api/next/v1"
    return api_next_url
