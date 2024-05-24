import requests
import configuration
import create_order

# Николай Чубриков, 16-я когорта — Финальный проект. Инженер по тестированию плюс

def get_created_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, params=create_order.track)


def test_1():
    response = get_created_order()
    assert response.status_code == 200
