import allure
import requests
from Sprint_7_api.project_url import Urls, Endpoints


class TestCheckOrderList:

    @allure.title('Cписок заказов успешно отображается')
    def test_list_order(self):
        response = requests.get(f'{Urls.URL}{Endpoints.CREATE_ORDER}')
        assert response.status_code == 200
        expected_order_keys = [
            "id",
            "courierId",
            "firstName",
            "lastName",
            "address",
            "metroStation",
            "phone",
            "rentTime",
            "deliveryDate",
            "track",
            "color",
            "comment",
            "createdAt",
            "updatedAt",
            "status"
        ]

        orders_data = response.json().get("orders", [])

        assert all(all(key in order.keys() for key in expected_order_keys) for order in
                   orders_data), "No orders returned or orders list is empty"
