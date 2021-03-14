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
    @classmethod
    def update(cls, secret_key=None, **kwargs):
        request = http.HTTPRequest(
            resource=cls,
            method="put",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


class PatchResourceMixin(object):
    @classmethod
    def patch(cls, secret_key=None, **kwargs):
        request = http.HTTPRequest(
            resource=cls,
            method="patch",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


class DeleteResourceMixin(object):
    @classmethod
    def delete(cls, secret_key=None, **kwargs):
        request = http.HTTPRequest(
            resource=cls,
            method="delete",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


class RetrieveResourceMixin(object):
    @classmethod
    def retrieve(cls, secret_key=None, **kwargs):
        request = http.HTTPRequest(
            resource=cls,
            method="get",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


class ListResourceMixin(object):
    @classmethod
    def list(cls, secret_key=None, **kwargs):
        request = http.HTTPRequest(
            resource=cls,
            method="get",
            secret_key=secret_key,
        )
        request = request.request(payload=kwargs)
        return request


class GenericResourceMixin(
    CreateResourceMixin,
    UpdateResourceMixin,
    DeleteResourceMixin,
    RetrieveResourceMixin,
    ListResourceMixin,
):
    pass
