import paymob
from paymob.http_mixins import GenericResourceMixin
from paymob.utils import resource_to_url


class HTTPBaseResource(object):
    """
    Base HTTP Resource class
    """

    RESOURCE_URI = None

    @classmethod
    def resource_url(cls):
        """
        Resource URL
        """
        if not cls.RESOURCE_URI:
            raise NotImplementedError("Resource class must have a RESOURCE_URI string.")
        return resource_to_url(cls.RESOURCE_URI)


class HTTPRequest(object):
    """
    Base HTTP Requester.
    """

    def __init__(self, secret_key, resource=None, api_version=None):
        self.secret_key = secret_key
        self.resource = resource
        self.api_version = api_version or paymob.api_version

    def request(self):
        """
        Send request.
        calls:
           - request_handler
        """
        pass

    def request_headers(self):
        """
        Set headers.
        :return:
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


class GenericHTTPResource(GenericResourceMixin, HTTPBaseResource):
    pass
