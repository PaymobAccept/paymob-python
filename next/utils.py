from next import API_VERSION


def next_api_version(version: str = None) -> str:
    """
    Next API version handler.
    :param version: str
    :return: str
    """
    return API_VERSION if not version else "v1"


def resource_to_url(resource: str) -> str:
    """
    Convert any Resource's classes name to a valid API URL.
    :param resource: str
    :return: str
    """
    return f"/{next_api_version()}/{resource}/"
