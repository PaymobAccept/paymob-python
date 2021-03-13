import pytest

import paymob
from paymob.http import GenericHTTPResource


@pytest.fixture(autouse=True)
def setup_next():
    paymob.secret_key = "HelloWorld"


class IntentionResource(GenericHTTPResource):
    RESOURCE_PATH = "intention"


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

        assert "must have a RESOURCE_PATH string." in str(exception.value)
