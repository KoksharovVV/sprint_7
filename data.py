import random


class TestDataUrl:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIER_URL = f'{BASE_URL}courier/'
    LOGIN_COURIER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    ORDER_URL = f'{BASE_URL}orders'


class TestOrderCreation:
    color_black = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-07-07",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
    color_black_and_gray = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-07-07",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK", "GRAY"
        ]
    }

    no_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-07-07",
        "comment": "Saske, come back to Konoha",
        "color": []
    }


class TestDataRegisterCourier:
    couriers_register_with_empty_login = {"login": "",
                                          "password": "1234",
                                          "firstName": f"firstName_{random.randint(1, 100)}"}
    couriers_register_with_empty_password = {"login": f"login_{random.randint(1, 100)}",
                                             "password": "",
                                             "firstName": f"firstName_{random.randint(1, 100)}"}
