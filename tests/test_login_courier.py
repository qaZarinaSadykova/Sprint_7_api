import allure
import requests
from Sprint_7_api.project_url import Urls, Endpoints
from Sprint_7_api.data_test import TestUsers


class TestLoginCourier:

    @allure.title('Успешная авторизация возвращает id')
    def test_courier_login_return_id(self):
        payload = TestUsers.positive_login
        response = requests.post(f'{Urls.URL}{Endpoints.LOGIN_COURIER}', json=payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Авторизация без логина - "Недостаточно данных для входа"')
    def test_courier_login_without_login_negative_result(self):
        payload = TestUsers.user_without_login
        response = requests.post(f'{Urls.URL}{Endpoints.LOGIN_COURIER}', json=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Авторизация без пароля - "Недостаточно данных для входа"')
    def test_courier_login_without_password_negative_result(self):
        payload = TestUsers.user_without_password
        response = requests.post(f'{Urls.URL}{Endpoints.LOGIN_COURIER}', json=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Авторизация неверным логином - "Учетная запись не найдена"')
    def test_courier_login_wrong_login_negative_result(self):
        payload = TestUsers.wrong_login
        response = requests.post(f'{Urls.URL}{Endpoints.LOGIN_COURIER}', json=payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Авторизация неверным паролем - "Учетная запись не найдена"')
    def test_courier_login_wrong_password_negative_result(self):
        payload = TestUsers.wrong_password
        response = requests.post(f'{Urls.URL}{Endpoints.LOGIN_COURIER}', json=payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
