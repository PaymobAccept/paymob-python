from paymob.http import HTTPBaseResource, HTTPRequest
from paymob.http_mixins import CreateResourceMixin, RetrieveResourceMixin, ListResourceMixin
import json

class Customer(CreateResourceMixin, RetrieveResourceMixin, ListResourceMixin, HTTPBaseResource):
    RESOURCE_PATH = "customer"

    @classmethod
    def retrieve(cls, reference, secret_key=None, **kwargs):
        """
        Retrieve resource

        :param secret_key: Paymob's secret key
        :param kwargs: dict
        """
        if reference is None or reference == "":
            return "You need to add a transaction reference."

        request = HTTPRequest(
            resource=cls,
            method="get",
            secret_key=secret_key,
        )
        request = request.request(reference=reference)
        return request

