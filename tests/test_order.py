import json
import allure
import pytest
import requests
from data_for_tests.data import OrderData, TextResponse
from assistants.endpoints import Endpoints
from assistants.urls import Urls


class TestCreateOrder:
    @allure.title('Заказ с правильными данными для проверки успешного создания')
    @allure.description('Запрос создания заказа с правильными данными для тестирования, подтверждение ответа')
    @pytest.mark.parametrize('color', [{"color": ["BLACK"]}, {"color": ["GREY"]},
                                       {"color": ["BLACK", "GRAY"]}, {"color": [""]}])
    def test_create_order_success(self, color):
        headers = {'Content-type': 'application/json'}
        data = OrderData.data
        data.update(color)
        data_dump = json.dumps(data)
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_order}', headers=headers, data=data_dump)
        assert response.status_code == 201 and TextResponse.track_in_order_list in response.text
