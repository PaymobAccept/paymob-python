secret_key = None
API_VERSION = "v1"
from .accept import *  # noqa


def api_base_url():
    API_NEXT_URL = "http://127.0.0.1:49152/api/next/v1"
    return API_NEXT_URL
