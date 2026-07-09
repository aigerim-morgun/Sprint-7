import pytest
import requests

from data import ORDER
from urls import BASE_URL, CREATE_ORDER


class TestCreateOrder:

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

        response = requests.post(
            BASE_URL + CREATE_ORDER,
            json=body
        )

        assert response.status_code == 201
        assert "track" in response.json()