from paymob.utils import resource_to_url


class HTTPResource(object):
    """
    Base HTTP Resource class
    """

    def get_http_url(self):
        """
        Resource URL
        """
        assert not self.RESOURCE, NotImplementedError(
            "Resource class must have a RESOURCE string."
        )
        return resource_to_url(self.RESOURCE)

    def get_headers(self):
        """
        Base request headers.
        """
        pass


class HTTPRequest(object):
    """
    Base HTTP Requester.
    """

    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def request(self):
        """
        Send request.
        calls:
           - request_handler
        """
        pass

    def request_handler(self):
        """
        Handle exceptions
        calls:
            - request_error_handler
        """
        pass

    def request_error_handler(self):
        """
        Handle Resources' errors.
        calls:
            - request_error_mapper and handle errors of any kind.
        """
        pass

    def request_error_mapper(self):
        """
        Request Error mapper based on response error code/message.
        """
        pass
