from paymob.http import HTTPBaseResource
from paymob.http_mixins import CreateResourceMixin


class Intention(CreateResourceMixin, HTTPBaseResource):
    RESOURCE_PATH = "intention"
