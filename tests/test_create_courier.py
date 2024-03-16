import allure
import requests
from Sprint_7_api.conftest import generate_random_string, create_test_data
from Sprint_7_api.project_url import Urls, Endpoints
from Sprint_7_api.data_test import TestUsers


class TestCreateCourier:

    @allure.title('Создание курьера - позитивный кейс')
    def test_create_courier_positive_result(self, generate_random_string, create_test_data):
        payload = create_test_data
        response = requests.post(f'{Urls.URL}{Endpoints.CREATE_COURIER}', json=payload)
        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title('Создание курьера без логина - "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_login_negative_result(self):
        payload = TestUsers.user_without_login
        response = requests.post(f'{Urls.URL}{Endpoints.CREATE_COURIER}', json=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Создание курьера без пароля - "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_password_negative_result(self):
        payload = TestUsers.user_without_password
        response = requests.post(f'{Urls.URL}{Endpoints.CREATE_COURIER}', json=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Создание курьера с повторяющимся логином - "Этот логин уже используется"')
    def test_create_courier_with_existing_login_negative_result(self):
        payload = TestUsers.user_with_existing_login
        response = requests.post(f'{Urls.URL}{Endpoints.CREATE_COURIER}', json=payload)
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

