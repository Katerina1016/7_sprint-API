import allure
import pytest
import requests
from assistants.data_helper import CourierData, Courier
from assistants.endpoints import Endpoints
from assistants.urls import Urls
from data_for_tests.data import TextResponse


class TestCourierLogin:
    @allure.title('Курьер с действительными данными для проверки входа в систему')
    @allure.description('Запрос на авторизацию курьера, проверка ответа, удаление нового курьера')
    def test_courier_login(self, courier):
        courier_data = courier
        response = Courier().login_and_get_courier_id(courier_data['data_for_tests'])
        assert response['status_code'] == 200
        assert response.get('id')
        Courier().delete_courier(response["id"])

    @allure.title('Проверка, не удается выполнить вход без логина/пароля')
    @allure.description('Запрос входа без логина/пароля, подтверждение ответа')
    @pytest.mark.parametrize('courier_data', [CourierData.invalid_data_without_login,
                             CourierData.invalid_data_without_password])
    def test_courier_login_params_missing(self, courier_data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.login_courier}', data=courier_data)
        assert response.status_code == 400
        assert TextResponse.insufficient_login_data_response in response.text

    @allure.title('Проверка ошибки при входе в систему с неверными данными для тестов')
    @allure.description('Запрос входа с неверными данными для проверки, подтверждение ответа')
    def test_courier_login_null_data(self):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.login_courier}', data=CourierData.null_courier_data)
        assert response.status_code == 404
        assert TextResponse.profile_not_found_response in response.text