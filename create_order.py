import configuration
import data
import requests


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body, headers=data.headers)


def get_created_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, params=track)
