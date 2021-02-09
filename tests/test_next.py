import pytest

import next


@pytest.fixture(autouse=True)
def setup_next():
    next.secret_key = "HelloWorld"


class TestNextSetup(object):
    def test_secret_key(self):
        """
        Test next scope.
        """
        assert next.secret_key == "HelloWorld"
