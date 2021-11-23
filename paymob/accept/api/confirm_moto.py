from paymob.http import HTTPBaseResource, HTTPRequest
from paymob.http_mixins import CreateResourceMixin
import json

class PayToken(CreateResourceMixin, HTTPBaseResource):
    RESOURCE_PATH = "intention/confirm-moto"

    @classmethod
    def create(cls, secret_key=None, path=None, **kwargs):
        """
        Create resource

        :param secret_key: Paymob's secret key
        :param kwargs: dict
        """
        error = []
        if len(kwargs) == 0:
            return {"Payload":"Some Parameters are missed"}
        if 'client_secret' not in kwargs:
            error.append({"client_secret":"This field is required"})
        if 'token' not in kwargs:
            error.append({"token":"This field is required"})
        if 'customer_id' not in kwargs:
            error.append({"customer_id":"This field is required"})
        if 'method' not in kwargs:
            error.append({"method":"This field is required"})

        if len(error) > 0:
           return json.dumps(error)
        error = []

        request = HTTPRequest(
            resource=cls,
            method="post",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


