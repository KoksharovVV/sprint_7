from helpers.helpers import login_courier
from data import TestDataLogin


class TestCourierLogin:
    def test_authorization_with_valid_login_and_password(self):
        response = login_courier(TestDataLogin.valid_login_and_valid_password)
        assert response.status_code == 200 and "id" in response.json()

    def test_authorization_with_invalid_login(self):
        response = login_courier(TestDataLogin.with_invalid_login)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    def test_authorization_with_password_is_invalid(self):
        response = login_courier(TestDataLogin.valid_login_and_invalid_password)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    def test_authorization_without_login(self):
        response = login_courier(TestDataLogin.without_login_valid_password)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    def test_authorization_without_password(self):
        response = login_courier(TestDataLogin.valid_login_without_password)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    def test_authorization_non_existent_user(self):
        response = login_courier(TestDataLogin.valid_login_without_password)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"
