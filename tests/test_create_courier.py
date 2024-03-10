import allure
import requests
import random
import string


class TestCreateCourier:

    @staticmethod
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    @staticmethod
    def create_courier(payload):
        return requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)

    @allure.title('Создание курьера - позитивный кейс')
    def test_create_courier_positive_result(self):
        payload = {field: self.generate_random_string(10) for field in ["login", "password", "firstName"]}
        response = self.create_courier(payload)
        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title('Создание курьера без логина - "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_login_negative_result(self):
        payload = {field: self.generate_random_string(10) for field in ["password", "firstName"]}
        response = self.create_courier(payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Создание курьера без пароля - "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_password_negative_result(self):
        payload = {field: self.generate_random_string(10) for field in ["login", "firstName"]}
        response = self.create_courier(payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Создание курьера с повторяющимся логином - "Этот логин уже используется"')
    def test_create_courier_with_existing_login_negative_result(self):
        payload = {"login": "eqrtttttter", "password": "dfghjklklk"}
        response = self.create_courier(payload)
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

