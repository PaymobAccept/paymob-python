from paymob.logging import *

from flask import Flask, jsonify
from flask_cors import CORS

import paymob

#live
paymob.secret_key = 'skl_eb7e7ac5117dcd6c0b7539a635f61764aca615bd3b63051606b845c30db3bff8'

#test

#paymob.secret_key = 'skt_c71983ae3738ba5eab3fd2a8b480992fe8927bba9dc34300049b840b6d3503cd'


app = Flask(__name__)
CORS(app)

# logging.basicConfig(
#     level=logging.DEBUG, format="%(levelname)s - %(name)s %(asctime)s - %(message)s"
# )
# logging.getLogger("paymob-next")


@app.route("/marketplace/secret/", methods=['GET'])
def secret():
    intent = paymob.accept.Intention.create(
        amount="300",
        currency="EGP",
        payment_methods=["card","kiosk"],
        items= [
    {
        "name": "ASC1124",
        "amount": "150",
        "description": "Smart Watch",
        "quantity": "1"
    },
    {
        "name": "ERT6565",
        "amount": "150",
        "description": "Power Bank",
        "quantity": "1"
    }
    ],
        billing_data={
            "apartment": "803",
            "email": "claudette09@exa.com",
            "floor": "42",
            "first_name": "Mohamed",
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
        extras= {
            "name": "test",
            "age": "30"
        },
        special_reference= "Special reference test 4"
    )
    log(
        "Intention Creation Response - {intent}".format(
            intent=intent
        ),
        "info",
    )
    return jsonify(intent)

@app.route("/marketplace/retrieve/", methods=['GET'])
def retrieve():
    retrieve_intent= paymob.accept.Intention.retrieve(
        reference="0cc46c79-e377-4c43-91c4-95f7a2fca151",
    )
    log(
        "Retrieve Response - {retrieve_intent}".format(
            retrieve_intent=retrieve_intent
        ),
        "info",
    )
    return retrieve_intent

@app.route("/marketplace/list/", methods=['GET'])
def list():
    list_intent= paymob.accept.Intention.list(
    )
    log(
        "List Response - {list_intent}".format(
            list_intent=list_intent
        ),
        "info",
    )
    return list_intent

@app.route("/marketplace/refund/", methods=['GET'])
def refund():
    refund_intent = paymob.accept.Refund.create(
        payment_reference= "14394788",
        amount_cents="300"
    )
    log(
        "Refund Response - {refund_intent}".format(
            refund_intent=refund_intent
        ),
        "info",
    )
    return refund_intent


@app.route("/marketplace/void/", methods=['GET'])
def void():
    void_intent= paymob.accept.Void.create(
        payment_reference="14394788"
    )
    log(
        "Intention Voided - {void_intent}".format(
            void_intent=void_intent
        ),
        "info",
    )
    return void_intent

@app.route("/marketplace/capture/", methods=['GET'])
def capture():
    capture_intent= paymob.accept.Capture.create(
        payment_reference="14394788",
        amount_cents="300"
    )
    log(
        "Intention Captured - {capture_intent}".format(
            capture_intent=capture_intent
        ),
        "info",
    )
    return capture_intent

if __name__ == "__main__":
    app.run(debug=True, port=8000)
