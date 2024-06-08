import allure
import requests
from assistants.endpoints import Endpoints
from assistants.urls import Urls
from data_for_tests.data import TextResponse


class TestOrderList:
    @allure.title('Получить список заказов для проверки')
    @allure.description('Получить список заказов, подтвердить ответ')
    def test_get_list_of_orders(self):
        response = requests.get(f'{Urls.SCOOTER_URL}{Endpoints.order_list}')
        assert response.status_code == 200
        assert TextResponse.track_in_order_list in response.text
