import create_order
import data


# Николай Чубриков, 16-я когорта — Финальный проект. Инженер по тестированию плюс


def test_get_order_by_track_success():
    response_order = create_order.post_new_order(data.order_body)
    track = {"t": response_order.json()["track"]}
    response = create_order.get_created_order(track)
    assert response.status_code == 200
