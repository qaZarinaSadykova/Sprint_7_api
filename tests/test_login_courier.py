import allure
import requests


class TestLoginCourier:

    @staticmethod
    def login_courier(payload):
        return requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

    @allure.title('Успешная авторизация возвращает id')
    def test_courier_login_return_id(self):
        payload = {
            "login": "yeymmcbbkx",
            "password": "ojugthnwnm"
        }
        response = self.login_courier(payload)

        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Авторизация без логина - "Недостаточно данных для входа"')
    def test_courier_login_without_login_negative_result(self):
        payload = {
            "login": "",
            "password": "ojugthnwnm"
        }
        response = self.login_courier(payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Авторизация без пароля - "Недостаточно данных для входа"')
    def test_courier_login_without_password_negative_result(self):
        payload = {
            "login": "yeymmcbbkx",
            "password": ""
        }
        response = self.login_courier(payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Авторизация неверным логином - "Учетная запись не найдена"')
    def test_courier_login_wrong_login_negative_result(self):
        payload = {
            "login": "00000000",
            "password": "ojugthnwnm"
        }
        response = self.login_courier(payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Авторизация неверным паролем - "Учетная запись не найдена"')
    def test_courier_login_wrong_password_negative_result(self):
        payload = {
            "login": "yeymmcbbkx",
            "password": "000000000"
        }
        response = self.login_courier(payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
