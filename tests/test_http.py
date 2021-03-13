import pytest

import paymob
from paymob.http import GenericHTTPResource


@pytest.fixture(autouse=True)
def setup_next():
    paymob.secret_key = "HelloWorld"


class IntentionResource(GenericHTTPResource):
    RESOURCE_URI = "intention"


class IntentionResourceWithoutURI(GenericHTTPResource):
    pass


class TestHttpResources(object):
    def test_generic_http_resource_url(self):
        intention = IntentionResource()
        assert intention.resource_url() == "/v1/intention/"

    def test_generic_http_resource_url_exception(self):
        intention = IntentionResourceWithoutURI()
        with pytest.raises(NotImplementedError) as exception:
            intention.resource_url()

        assert "must have a RESOURCE_URI string." in str(exception.value)
