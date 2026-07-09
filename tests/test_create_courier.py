import requests

from helpers import generate_random_string
from urls import BASE_URL, CREATE_COURIER


class TestCreateCourier:

    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_duplicate_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        requests.post(BASE_URL + CREATE_COURIER, data=payload)

        response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    def test_create_without_login(self):
        payload = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert response.status_code == 400

    def test_create_without_password(self):
        payload = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert response.status_code == 400


    def test_create_without_required_fields(self):
        payload = {}

        response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert response.status_code == 400