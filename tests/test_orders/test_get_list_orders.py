from helpers.helpers import get_list_orders


class TestOrderList:
    def test_getting_list_of_orders(self):
        response = get_list_orders()
        assert response.status_code == 200 and "orders" in response.json()
