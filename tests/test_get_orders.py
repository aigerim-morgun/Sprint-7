import allure
import requests

from urls import BASE_URL, GET_ORDERS


class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders(self):

        with allure.step("Получить список заказов"):
            response = requests.get(BASE_URL + GET_ORDERS)

        body = response.json()

        assert response.status_code == 200
        assert "orders" in body