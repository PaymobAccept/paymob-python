import logging

from flask import Flask, jsonify
from flask_cors import CORS

import paymob

paymob.secret_key = (
    "skt_a2ed304e7b12bbdcf41617ed6eb52f7a63580bd09a4579a2b253f199999e58e5"
)

app = Flask(__name__)
CORS(app)

logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)s - %(name)s %(asctime)s - %(message)s"
)
logging.getLogger("paymob-next")


@app.route("/secret", methods=["GET"])
def secret():
    intent = paymob.accept.Intention.create(
        amount=1000,
        currency="EGP",
        payment_methods=["card", "kiosk"],
        billing_data={
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
        delivery_needed=False,
    )
    print(intent)
    return jsonify(client_secret=intent.get("client_secret"))


if __name__ == "__main__":
    app.run(debug=True, port=10000)

"""
{
        "amount": 1000,
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
"""
