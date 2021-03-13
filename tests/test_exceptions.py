from http import HTTPStatus
from paymob.exceptions import UserNotAllowed


class TestUserNotAllowed(object):
    def test_user_not_allowed(self):
        assert UserNotAllowed.status_code == HTTPStatus.FORBIDDEN
