import logging

from flask import Flask, jsonify
from flask_cors import CORS

import paymob

paymob.secret_key = 'skl_523053414432477c0ba43c1005a57230db53c56f577fbdc1fe93211ed3b53838'
app = Flask(__name__)
CORS(app)

logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)s - %(name)s %(asctime)s - %(message)s"
)
logging.getLogger("paymob-next")


@app.route("/marketplace/secret/", methods=["GET"])
def secret():
    intent = paymob.accept.Intention.create(
        amount="100",
        currency="EGP",
        payment_methods=["card"],
        items= [
    {
        "name": "ASC1515",
        "amount": "50",
        "description": "Smart Watch",
        "quantity": "1"
    },
    { 
        "name": "ERT6565",
        "amount": "50",
        "description": "Power Bank",
        "quantity": "1"
    }
    ],
        billing_data={
            "apartment": "803",
            "email": "claudette09@exa.com",
            "floor": "42",
            "first_name": "Clifford",
            "street": "Ethan Land",
            "building": "8028",
            "phone_number": "9135210487",
            "shipping_method": "PKG",
            "postal_code": "01898",
            "city": "Jaskolskiburgh",
            "country": "CR",
            "last_name": "Nicolas",
            "state": "Utah",
        },
        customer={"first_name": "misrax", "last_name": "misrax", "email": "misrax@misrax.com"},
        delivery_needed=False,
    )
    return jsonify(client_secret=intent.get("client_secret"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
