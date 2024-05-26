import configuration
import data
import requests


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body, headers=data.headers)


response = post_new_order(data.order_body)
track = response.json()["track"]

