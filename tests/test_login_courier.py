import allure
import requests

from urls import BASE_URL, LOGIN_COURIER


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, create_courier):
        payload = {
            "login": create_courier[0],
            "password": create_courier[1]
        }

        with allure.step("Авторизовать курьера"):
            response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 200
        assert "id" in body

    @allure.title("Авторизация без логина")
    def test_login_without_login(self):
        payload = {
            "password": "1234"
        }

        with allure.step("Отправить запрос без логина"):
            response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 400
        assert "message" in body

    @allure.title("Авторизация без пароля")
    def test_login_without_password(self, create_courier):
        payload = {
            "login": create_courier[0]
        }

        with allure.step("Отправить запрос без пароля"):
            response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        assert response.status_code in [400, 504]

        if response.status_code == 400:
            body = response.json()
            assert "message" in body

    @allure.title("Авторизация с неверным логином")
    def test_login_with_wrong_login(self, create_courier):
        payload = {
            "login": "wrong_login",
            "password": create_courier[1]
        }

        with allure.step("Авторизоваться с неверным логином"):
            response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация с неверным паролем")
    def test_login_wrong_password(self, create_courier):
        payload = {
            "login": create_courier[0],
            "password": "wrong_password"
        }

        with allure.step("Авторизоваться с неверным паролем"):
            response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_nonexistent_user(self):
        payload = {
            "login": "random_login",
            "password": "random_password"
        }

        with allure.step("Авторизоваться несуществующим пользователем"):
            response = requests.post(BASE_URL + LOGIN_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Учетная запись не найдена"