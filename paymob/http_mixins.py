import requests

from paymob.utils import api_base_url


class CreateResourceMixin(object):
    def create(self, secret_key=None, **kwargs):
        request = requests.post(
            api_base_url() + "intentions/create/",
            json=kwargs,
            headers={
                "Authorization": "Token {secret_key}".format(secret_key=secret_key)
            },
        )
        intent_response = request.json()
        print(intent_response)
        return intent_response


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
