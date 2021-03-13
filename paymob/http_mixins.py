from paymob import http


class CreateResourceMixin(object):
    @classmethod
    def create(cls, secret_key=None, **kwargs):
        request = http.HTTPRequest(
            resource=cls,
            method="post",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


class UpdateResourceMixin(object):
    def update(self, secret_key=None, **kwargs):
        pass


class DeleteResourceMixin(object):
    def delete(self, secret_key=None, **kwargs):
        pass


class RetrieveResourceMixin(object):
    def retrieve(self, secret_key=None, **kwargs):
        pass


class ListResourceMixin(object):
    def list(self, secret_key=None, **kwargs):
        pass


class GenericResourceMixin(
    CreateResourceMixin,
    UpdateResourceMixin,
    DeleteResourceMixin,
    RetrieveResourceMixin,
    ListResourceMixin,
):
    pass
