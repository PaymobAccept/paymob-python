class CreateResourceMixin(object):
    def create(self, secret_key=None, **kwargs):
        pass


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
