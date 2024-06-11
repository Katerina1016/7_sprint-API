from faker import Faker
import requests
from assistants.endpoints import Endpoints
from assistants.urls import Urls
import allure


class DataCreateCourier:
    @staticmethod
    @allure.step("Create fake valid data to create courier")
    def generate_fake_valid_info_to_create_courier():
        fake = Faker('ru_RU')
        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()
        data = {
            'login': login,
            'firstname': first_name,
            'password': password
        }

        return data

    @staticmethod
    @allure.step("Create fake invalid data without login to create courier")
    def generate_fake_info_to_create_courier_without_login():
        fake = Faker('ru_RU')
        password = fake.password()
        first_name = fake.first_name()
        data = {
            'login': "",
            'firstname': first_name,
            'password': password
        }

        return data

    @staticmethod
    @allure.step("Create fake invalid data without password to create courier")
    def generate_fake_info_to_create_courier_without_password():
        fake = Faker('ru_RU')
        login = fake.user_name()
        first_name = fake.first_name()
        data = {
            'login': login,
            'firstname': first_name,
            'password': ""
        }

        return data

    @staticmethod
    @allure.step("Retrieve auth data of unexistant courier")
    def get_null_data_courier():
        data = {
            'login': 'test',
            'password': 'test'
        }

        return data


class CourierData:
    valid_data_for_login = DataCreateCourier.generate_fake_valid_info_to_create_courier()
    invalid_data_without_login = DataCreateCourier.generate_fake_info_to_create_courier_without_login()
    invalid_data_without_password = DataCreateCourier.generate_fake_info_to_create_courier_without_password()
    null_courier_data = DataCreateCourier.get_null_data_courier()


class Courier:
    @staticmethod
    @allure.step("Create valid data,register a courier, retrieve courier data")
    def registration_and_get_courier_data():
        data = DataCreateCourier.generate_fake_valid_info_to_create_courier()
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data_for_tests": data}

    @staticmethod
    @allure.step("Authorize a courier, retrieve courier's ID")
    def login_and_get_courier_id(data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.login_courier}', data=data)
        return {"id": response.json()["id"], "response_text": response.text, "status_code": response.status_code}

    @staticmethod
    @allure.step("Delete courier")
    def delete_courier(id):
        response = requests.delete(f'{Urls.SCOOTER_URL}{Endpoints.delete_courier}{id}')
        return {'response_text': response.text, 'status_code': response.status_code}
