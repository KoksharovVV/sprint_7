import requests
import random
import string
from data import TestDataUrl
from data import TestOrderCreation


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def register_courier(payload=None):
    if payload is None:
        payload = {}
        payload["login"] = payload.get("login", generate_random_string(10))
        payload["password"] = payload.get("password", generate_random_string(10))
        payload["firstName"] = payload.get("firstName", generate_random_string(10))
    response = requests.post(TestDataUrl.COURIER_URL, data=payload)
    return {"login": payload["login"], "password": payload["password"], "first_name": payload["firstName"],
            "response": response}


def login_courier(credentials):
    payload = {
        "login": credentials["login"],
        "password": credentials["password"]
    }
    response = requests.post(TestDataUrl.LOGIN_COURIER_URL, data=payload)
    return response


def create_order(payload=None):
    if payload is None:
        payload = TestOrderCreation.color_black
    response = requests.post(TestDataUrl.ORDER_URL, json=payload)
    return response


def get_list_orders():
    order_list = requests.get(TestDataUrl.ORDER_URL)
    return order_list


def delete_courier(id_courier=None):
    response = requests.delete(f"{TestDataUrl.COURIER_URL}{id_courier}")
    return response
