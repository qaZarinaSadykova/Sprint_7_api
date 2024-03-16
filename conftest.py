import random
import string
import pytest
import requests
from Sprint_7_api.project_url import Urls, Endpoints

@pytest.fixture
def generate_random_string():
    """Фикстура для генерации случайной строки"""
    def _generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return _generate_random_string


@pytest.fixture
def create_test_data(request, generate_random_string):
    """Создание тестовых данных перед тестом"""
    test_data = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
    }

    def _delete_test_data():
        """Удаление тестовых данных после теста"""
        response = requests.post(f'{Urls.URL}{Endpoints.LOGIN_COURIER}', json=test_data)
        assert response.status_code == 200
        assert 'id' in response.json()
        courier_id = response.json()["id"]
        response = requests.delete(f'{Urls.URL}{Endpoints.CREATE_COURIER}/{courier_id}')
        assert response.status_code == 200
        assert 'id' not in response.json()

    """Добавление функции удаления в финализатор фикстуры"""
    request.addfinalizer(_delete_test_data)

    return test_data
