Sprint-7

Описание проекта

Автоматизированное тестирование API сервиса Яндекс Самокат.

В проекте реализованы проверки следующих ручек API: • создание курьера; • авторизация курьера; • создание заказа; • получение списка заказов.

Для тестирования используются: • Python 3 • pytest • requests • Allure

Структура проекта Sprint_7 ├── tests │ ├── test_create_courier.py │ ├── test_login_courier.py │ ├── test_create_order.py │ └── test_get_orders.py ├── conftest.py ├── data.py ├── helpers.py ├── urls.py ├── requirements.txt └── README.md

Установка зависимостей pip install -r requirements.txt

Запуск тестов pytest

Запуск с генерацией отчёта Allure pytest --alluredir=allure-results

Просмотр отчёта Allure allure serve allure-results# Sprint-7
