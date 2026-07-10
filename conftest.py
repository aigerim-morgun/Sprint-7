import pytest
import requests

from courier_methods import register_new_courier_and_return_login_password
from urls import BASE_URL, LOGIN_COURIER, CREATE_COURIER


@pytest.fixture
def create_courier():
    courier = register_new_courier_and_return_login_password()

    yield courier

    login_data = {
        "login": courier[0],
        "password": courier[1]
    }

    response = requests.post(
        BASE_URL + LOGIN_COURIER,
        data=login_data
    )

    courier_id = response.json()["id"]

    requests.delete(
        BASE_URL + CREATE_COURIER + f"/{courier_id}"
    )
