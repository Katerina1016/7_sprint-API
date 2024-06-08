import pytest
from assistants.data_helper import Courier


@pytest.fixture()
def courier():
    courier_create = Courier().registration_and_get_courier_data()
    yield courier_create
