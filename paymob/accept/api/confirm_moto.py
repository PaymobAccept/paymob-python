from paymob.http import HTTPBaseResource
from paymob.http_mixins import CreateResourceMixin


class TokenPay(CreateResourceMixin, HTTPBaseResource):
    RESOURCE_PATH = "intention/confirm-moto"


