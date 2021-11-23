from paymob.logging import *

from flask import Flask, jsonify
from flask_cors import CORS

import paymob


#live secret key
paymob.secret_key = 'skl_51bf49f38681a7d859fbb7a48d43df747877e66e906a1851efad3c8f427c1082'

#test secret key
#paymob.secret_key = 'skt_910f3e11fce0ea90e2af1683bab7439108cdb0e36333377f52422932ede25ac0'

paymob.base_url = "https://flashapi.paymob.com"
paymob.next_version = "v1"


app = Flask(__name__)
CORS(app)

# logging.basicConfig(
#     level=logging.DEBUG, format="%(levelname)s - %(name)s %(asctime)s - %(message)s"
# )
# logging.getLogger("paymob-next")


@app.route("/marketplace/secret/", methods=['GET'])
def secret():
    intent = paymob.accept.Intention.create(
        amount="100",
        currency="EGP",
        payment_methods=[1599970],
        items= [
    {
        "name": "ASC1124",
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
            "first_name": "Mohamed",
            "street": "Ethan Land",
            "building": "8028",
            "phone_number": "+201010101010",
            "shipping_method": "PKG",
            "postal_code": "01898",
            "city": "Jaskolskiburgh",
            "country": "CR",
            "last_name": "Nicolas",
            "state": "Utah",
        },
        customer={
            "first_name": "youssef", "last_name": "tarek", "email": "youssef@tarek.com","phone_number":"+201010101010",
            "extras":{
                "surname":"Abdelsattar"
            }

        },
        delivery_needed=False,
        extras= {
            "name": "test",
            "age": "30"
        },
        #special_reference= "Special reference test 4"
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
        reference="f4ec76dd-214a-4af6-997c-d05ee62e4140",
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
        payment_reference= "17653797",
        amount_cents="50"
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
        payment_reference="18157980"
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
        payment_reference="17653797",
        amount_cents="50"
    )
    log(
        "Intention Captured - {capture_intent}".format(
            capture_intent=capture_intent
        ),
        "info",
    )
    return capture_intent

@app.route("/marketplace/paytoken/", methods=['GET'])
def pay_token():

    savedpay= paymob.accept.PayToken.create(

            client_secret = "ckl_77bacfb1a13e04786f7a6226b6d8e244",
            token_id="123456",
            token="e29ac6d6676da32f228c7fe5a1a111694978f14ea686915f42fa53e93",
            customer_id= "baaba246-895c-4dfd-877b-c1ae10069188",
            method= "card-moto",
            payment_method_id= 1599970


    )
    log(
        "Payment Response - {savedpay}".format(
            savedpay=savedpay
        ),
        "info",
    )
    return savedpay

@app.route("/marketplace/customer_details/", methods=['GET'])
def customer_retrieve():
    customer= paymob.accept.Customer.retrieve(
     reference= "69260c5f-101c-49d9-a509-368c593b9a99"
    )
    log(
        "Customer Details Response - {customer}".format(
            customer=customer
        ),
        "info",
    )
    return customer

@app.route("/marketplace/customers_list/", methods=['GET'])
def customer_list():
    customers= paymob.accept.Customer.list(

    )
    log(
        "Customers List Response - {customers}".format(
            customers=customers
        ),
        "info",
    )
    return customers

if __name__ == "__main__":
    app.run(debug=True, port=8000)
