import allure
import requests


class TestCheckOrderList:
    @staticmethod
    def courier_order_list():
        return requests.get('http://qa-scooter.praktikum-services.ru/api/v1/orders')

    @allure.title('Cписок заказов успешно отображается')
    def test_list_order(self):
        response = self.courier_order_list()
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

        if orders_data and len(orders_data) > 0:
            for order in orders_data:
                order_keys = order.keys()
                assert all(key in order_keys for key in expected_order_keys)
        else:
            assert False, "No orders returned or orders list is empty"
