import allure
import pytest
import requests

from data import ORDER
from urls import BASE_URL, CREATE_ORDER


class TestCreateOrder:

    @allure.title("Создание заказа с разными цветами")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    def test_create_order(self, color):
        body = ORDER.copy()
        body["color"] = color

        with allure.step("Создать заказ"):
            response = requests.post(
                BASE_URL + CREATE_ORDER,
                json=body
            )

        response_body = response.json()

        assert response.status_code == 201
        assert "track" in response_body