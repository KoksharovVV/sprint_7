import requests
from helpers.helpers import register_courier
from data import TestDataUrl, TestDataRegisterCourier


class TestCourierRegistration:
    def test_successful_courier_registration(self):
        response = register_courier()
        assert response["response"].status_code == 201 and response["response"].json()["ok"] == True

    def test_missing_data_courier_registration_login(self):
        response = register_courier(TestDataRegisterCourier.couriers_register_with_empty_login)
        assert response["response"].status_code == 400 and "Недостаточно данных для создания учетной записи" in \
               response["response"].text

    def test_missing_data_courier_registration_password(self):
        response = register_courier(TestDataRegisterCourier.couriers_register_with_empty_password)
        assert response["response"].status_code == 400 and "Недостаточно данных для создания учетной записи" in \
               response["response"].text

    def test_duplicate_login_courier_registration(self):
        first_courier = register_courier()
        response = requests.post(TestDataUrl.COURIER_URL, data=first_courier)
        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется"
