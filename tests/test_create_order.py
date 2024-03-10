
import allure
import pytest
import requests


class TestCreateOrder:

    @staticmethod
    def request_order(order_data):
        return requests.post('http://qa-scooter.praktikum-services.ru/api/v1/orders', json=order_data)

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

        response = self.request_order(order_data)
        assert response.status_code == 201 and 'track' in response.text
