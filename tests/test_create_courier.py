import allure
import pytest
import requests
from assistants.data_helper import CourierData, Courier
from assistants.endpoints import Endpoints
from assistants.urls import Urls
from data_for_tests.data import TextResponse


class TestCourierCreate:
    @allure.title('Проверка создания курьера')
    @allure.description('Запрос на создание курьера, проверка ответа')
    def test_registration_courier_successfully(self, courier):
        courier_data = courier
        assert courier_data['status_code'] == 201
        assert TextResponse.response_successful_operation in courier_data['response_text']
        courier_login = Courier().login_and_get_courier_id(courier_data["data_for_tests"])
        Courier().delete_courier(courier_login["id"])

    @allure.title('Проверка ошибки регистрации двух одинаковых курьеров')
    @allure.description('Запрос на создание одинакового курьера, проверку ожидаемой ошибки и удаление нового курьера')
    def test_double_registration_courier_failed(self, courier):
        courier_data = courier
        first_courier_id = Courier().login_and_get_courier_id(courier_data["data_for_tests"])
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=courier_data["data_for_tests"])
        assert response.status_code == 409
        assert TextResponse.reusing_the_login in response.text
        Courier().delete_courier(first_courier_id["id"])

    @allure.title('Проверка ошибки при регистрации курьера без логина/пароля')
    @allure.description('Запрос на создание курьера без логина/пароля и подтверждение ответа')
    @pytest.mark.parametrize('courier_data', [CourierData.invalid_data_without_login,
                             CourierData.invalid_data_without_password])
    def test_registration_without_data_failed(self, courier_data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)
        assert response.status_code == 400
        assert TextResponse.response_insufficient_data in response.text
