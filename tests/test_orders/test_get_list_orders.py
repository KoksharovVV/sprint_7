import allure
from helpers.helpers import get_list_orders


class TestOrderList:
    @allure.title("Тест получения списка заказов")
    @allure.description("Проверка статус кода и ответа при запросе списка заказов")
    def test_getting_list_of_orders(self):
        response = get_list_orders()
        assert response.status_code == 200 and "orders" in response.json()
