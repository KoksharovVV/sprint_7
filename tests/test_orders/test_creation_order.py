import allure
import pytest
from helpers.helpers import create_order
from data import TestOrderCreation


class TestPostCreatingOrder:

    @allure.title("Тест создания заказа с выбором цвета")
    @allure.description("Проверка статус кода и ответа при создании заказа с выбором разных цветов")
    @pytest.mark.parametrize("colors", [
        TestOrderCreation.color_black,
        TestOrderCreation.color_black_and_gray,
        TestOrderCreation.no_color], ids=[
        "color - BLACK",
        "color - GREY",
        "color - NO COLOR"
    ])
    def test_selection_color(self, colors):
        response = create_order(colors)
        assert response.status_code == 201 and "track" in response.json()
