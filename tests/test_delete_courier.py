import allure
from assistants.data_helper import Courier
from data_for_tests.data import TextResponse


class TestDeleteCourier:
    @allure.title('Проверка удаления курьера')
    @allure.description('Запрос на удаление курьера, проверка ответа')
    def test_courier_delete_success(self, courier):
        courier_id = courier
        courier_login = Courier().login_and_get_courier_id(courier_id["data_for_tests"])
        response = Courier().delete_courier(courier_login["id"])
        assert response["status_code"] == 200
        assert TextResponse.response_successful_operation in response['response_text']

    @allure.title('Проверка ошибки удаления курьера с недействительным идентификатором')
    @allure.description('Запрос на удаление курьера с неверным идентификатором, проверка ответа')
    def test_courier_with_invalid_id_deletion_failed(self):
        invalid_id = '111111'
        response = Courier().delete_courier(invalid_id)
        assert response['status_code'] == 404
        assert TextResponse.response_not_courier_id in response['response_text']

    @allure.title('Проверка ошибки при удалении курьера без удостоверения личности')
    @allure.description('Запрос на удаление курьера без удостоверения личности, проверка ответа')
    def test_delete_courier_without_id_failed(self):
        courier_id = None
        response = Courier().delete_courier(courier_id)
        assert response['status_code'] == 500
        assert TextResponse.null_id_deletion in response['response_text']
