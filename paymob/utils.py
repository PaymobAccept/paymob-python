from paymob import api_version


def next_api_version(version=None):
    """
    Next API version handler.
    :param version: str
    :return: str
    """
    return api_version if not version else "v1"


def resource_to_url(resource):
    """
    Convert any Resource's classes name to a valid API URL.
    :param resource: str
    :return: str
    """
    return f"/{next_api_version()}/{resource}/"


def api_base_url():
    """

    :return: str api_next_url
    """
    api_next_url: str = "http://127.0.0.1:49152/api/next"
    return api_next_url
