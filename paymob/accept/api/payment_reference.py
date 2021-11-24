from paymob.http import HTTPBaseResource,HTTPRequest
from paymob.http_mixins import CreateResourceMixin

class Refund(CreateResourceMixin, HTTPBaseResource):
    RESOURCE_PATH= "payment-reference/refund"

    @classmethod
    def create(cls, secret_key=None, path=None, **kwargs):
        """
        Create resource

        :param secret_key: Paymob's secret key
        :param kwargs: dict
        """

        if len(kwargs) == 0:
            return {"Payload": "Some Parameters are missed."}
        if 'payment_reference' not in kwargs:
            return {"payment_reference": "This field is required."}
        if 'amount_cents' not in kwargs:
            return {"amount_cents": "This field is required."}


        request = HTTPRequest(
            resource=cls,
            method="post",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


class Void(CreateResourceMixin,HTTPBaseResource):
    RESOURCE_PATH= "payment-reference/void"

    @classmethod
    def create(cls, secret_key=None, path=None, **kwargs):
        """
        Create resource

        :param secret_key: Paymob's secret key
        :param kwargs: dict
        """
        if len(kwargs) == 0:
            return {"Payload": "Some Parameters are missed."}
        if 'payment_reference' not in kwargs:
            return {"payment_reference": "This field is required."}


        request = HTTPRequest(
            resource=cls,
            method="post",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


class Capture(CreateResourceMixin,HTTPBaseResource):
    RESOURCE_PATH= "payment-reference/capture"

    @classmethod
    def create(cls, secret_key=None, path=None, **kwargs):
        """
        Create resource

        :param secret_key: Paymob's secret key
        :param kwargs: dict
        """
        if len(kwargs) == 0:
            return {"Payload": "Some Parameters are missed."}
        if 'payment_reference' not in kwargs:
            return {"payment_reference": "This field is required."}
        if 'amount_cents' not in kwargs:
            return {"amount_cents": "This field is required."}

        request = HTTPRequest(
            resource=cls,
            method="post",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request
