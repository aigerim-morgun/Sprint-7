import requests

from urls import BASE_URL, LOGIN_COURIER


class TestLoginCourier:

    def test_login_success(self, create_courier):
        payload = {
            "login": create_courier[0],
            "password": create_courier[1]
        }

        response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        assert response.status_code == 200
        assert "id" in response.json()

    def test_login_without_login(self):
        payload = {
            "password": "1234"
        }

        response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        assert response.status_code == 400

    def test_login_without_password(self, create_courier):
        payload = {
            "login": create_courier[0]
        }

        response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        assert response.status_code in [400, 504]

    def test_login_with_wrong_login(self, create_courier):
        payload = {
            "login": "wrong_login",
            "password": create_courier[1]
        }

        response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_wrong_password(self, create_courier):
        payload = {
            "login": create_courier[0],
            "password": "wrong_password"
        }

        response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_nonexistent_user(self):
        payload = {
            "login": "random_login",
            "password": "random_password"
        }

        response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"