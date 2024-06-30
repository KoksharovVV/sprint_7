import allure
from helpers.helpers import login_courier
from data import TestDataLogin


class TestCourierLogin:
    @allure.title("Тест успешной авторизации")
    @allure.description("Проверка статус кода и ответа при авторизации только с обязательными полями")
    def test_authorization_with_valid_login_and_password(self):
        response = login_courier(TestDataLogin.valid_login_and_valid_password)
        assert response.status_code == 200 and "id" in response.json()

    @allure.title("Тест ошибки авторизации с ошибкой в логине")
    @allure.description("Проверка статус кода и ответа при авторизации с опечаткой в логине")
    def test_authorization_with_invalid_login(self):
        response = login_courier(TestDataLogin.with_invalid_login)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Тест ошибки авторизации с ошибкой в пароле")
    @allure.description("Проверка статус кода и ответа при авторизации с опечаткой в пароле")
    def test_authorization_with_password_is_invalid(self):
        response = login_courier(TestDataLogin.valid_login_and_invalid_password)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Тест ошибки авторизации без логина")
    @allure.description("Проверка статус кода и ответа при авторизации без логина")
    def test_authorization_without_login(self):
        response = login_courier(TestDataLogin.without_login_valid_password)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Тест ошибки авторизации без пароля")
    @allure.description("Проверка статус кода и ответа при авторизации без пароля")
    def test_authorization_without_password(self):
        response = login_courier(TestDataLogin.valid_login_without_password)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Тест ошибки авторизации для несуществующей пары логин-пароль ")
    @allure.description("Проверка статус кода и ответа при авторизации с несуществующей парой логин-пароль")
    def test_authorization_non_existent_user(self):
        response = login_courier(TestDataLogin.non_existent_user)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
