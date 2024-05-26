import requests
import configuration
import create_order

# Николай Чубриков, 16-я когорта — Финальный проект. Инженер по тестированию плюс


def get_created_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))


track = create_order.track


def test_get_order_by_track_success():
    response = get_created_order(track)
    assert response.status_code == 200
