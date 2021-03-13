def next_api_version():
    """
    Next API version handler.
    :return: str
    """
    return "v1"


def resource_to_url(resource):
    """
    Convert any Resource's classes name to a valid API URL.
    :param resource: str
    :return: str
    """
    return "/{next_api_version}/{resource}/".format(
        next_api_version=next_api_version(), resource=resource
    )


def api_base_url():
    """

    :return: str api_next_url
    """
    api_next_url = "http://127.0.0.1:8000/api/next"
    return api_next_url
