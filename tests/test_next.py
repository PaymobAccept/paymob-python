import pytest

import paymob


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
        assert paymob.api_base_url() == "http://127.0.0.1:49152/api/next/v1"
