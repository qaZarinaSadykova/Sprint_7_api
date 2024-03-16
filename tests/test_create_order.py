
import allure
import pytest
import requests
from Sprint_7_api.project_url import Urls, Endpoints


class TestCreateOrder:

    @pytest.mark.parametrize("color", ["BLACK", "GREY", "BLACK, GREY", "RED", " ", None])
    @allure.title('Создание заказа в разрезе цвета')
    def test_create_order_different_colors(self, color):
        order_data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                color
            ]
        }

        response = requests.post(f'{Urls.URL}{Endpoints.CREATE_ORDER}', json=order_data)
        assert response.status_code == 201 and 'track' in response.text
