import requests

from urls import BASE_URL, GET_ORDERS


class TestGetOrders:

    def test_get_orders(self):
        response = requests.get(BASE_URL + GET_ORDERS)

        assert response.status_code == 200
        assert "orders" in response.json()