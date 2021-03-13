import pytest

import paymob
from paymob.utils import api_base_url, next_api_version


@pytest.fixture(autouse=True)
def setup_next():
    paymob.secret_key = "HelloWorld"


class TestNextSetup(object):
    def test_secret_key(self):
        """
        Test next scope.
        """
        assert paymob.secret_key == "HelloWorld"

    def test_api_next_url(self):
        """
        Test Next API URL
        """
        assert api_base_url() == "http://127.0.0.1:8000/api/next"

    def test_api_version(self):
        """
        Test Next API version
        """
        assert next_api_version() == "v1"
