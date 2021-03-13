import requests

import paymob
from paymob.http import GenericHTTPResource


class Intention(GenericHTTPResource):
    RESOURCE_URI = "intention"

    def delete(**kwargs):
        pass

    def create(**kwargs):
        """
        Create payment intention.
        :param kwargs:
        :return:
        """
        intention_payload = {
            "amount": kwargs.get("amount"),
            "currency": "EGP",
            "delivery_needed": "false",
            "shipping_data": {
                "apartment": "1565162",
                "email": "abdulrahman@weaccept.co",
                "floor": "11",
                "first_name": "abdulrahman",
                "street": "Wadi el Nile",
                "state": "Cairo",
                "building": "5",
                "phone_number": "01011994353",
                "city": "Cairo",
                "country": "EG",
                "last_name": "Khalifa",
            },
            "items": [
                {
                    "name": "ASC1515",
                    "amount": "500000",
                    "description": "Smart Watch",
                    "quantity": "1",
                },
                {
                    "name": "ERT6565",
                    "amount": "200000",
                    "description": "Power Bank",
                    "quantity": "1",
                },
            ],
            "payment_methods": ["card", "kiosk"],
            "shipping_details": {
                "notes": " im so tired ",
                "number_of_packages": 1,
                "weight": 1,
                "weight_unit": "Kilogram",
                "length": 1,
                "width": 1,
                "height": 1,
                "contents": "product of some sorts",
            },
            "billing_data": {
                "apartment": "803",
                "email": "claudette09@exa.com",
                "floor": "42",
                "first_name": "Clifford",
                "street": "Ethan Land",
                "building": "8028",
                "phone_number": "+86(8)9135210487",
                "shipping_method": "PKG",
                "postal_code": "01898",
                "city": "Jaskolskiburgh",
                "country": "CR",
                "last_name": "Nicolas",
                "state": "Utah",
            },
        }

        intent = requests.post(
            paymob.api_base_url() + "intentions/create/",
            json=intention_payload,
            headers={"Authorization": f"Token {paymob.secret_key}"},
        )
        intent_response = intent.json()
        print(intent_response)
        return intent_response
