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
