import allure
import requests

from helpers import generate_random_string
from urls import BASE_URL, CREATE_COURIER


class TestCreateCourier:

    @allure.title("Создание нового курьера")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        with allure.step("Отправить запрос на создание курьера"):
            response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 201
        assert body == {"ok": True}

    @allure.title("Создание дубликата курьера")
    def test_create_duplicate_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        with allure.step("Создать курьера"):
            requests.post(BASE_URL + CREATE_COURIER, data=payload)

        with allure.step("Повторно создать того же курьера"):
            response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 409
        assert body["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера без логина")
    def test_create_without_login(self):
        payload = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        with allure.step("Отправить запрос без логина"):
            response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 400
        assert "message" in body

    @allure.title("Создание курьера без пароля")
    def test_create_without_password(self):
        payload = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        with allure.step("Отправить запрос без пароля"):
            response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 400
        assert "message" in body

    @allure.title("Создание курьера без обязательных полей")
    def test_create_without_required_fields(self):
        payload = {}

        with allure.step("Отправить пустой запрос"):
            response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        body = response.json()

        assert response.status_code == 400
        assert "message" in body