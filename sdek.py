# -*- coding: utf-8 -*-
import requests


height = length = width = "10"
weight = "1.5"


def get_sdek(sender_city_name, receiver_city_name):
    url = 'http://integration.cdek.ru/v1/location/cities/json'
    response = requests.get(url=url, params={'cityName': sender_city_name}).json()
    sender_city_code = response[0]['cityCode']
    response = requests.get(url=url, params={'cityName': receiver_city_name}).json()
    receiver_city_code = response[0]['cityCode']
    header = {
        "Content-Type": "application/json"
    }
    body = {
        "version": "1.0",
        "senderCityId": sender_city_code,
        "receiverCityId": receiver_city_code,
        "currency": "RUB",
        "tariffList": [
            {
                "id": 5
            },
            {
                "id": 10
            }
        ],
        "goods": [
            {
                "weight": weight,
                "length": length,
                "width": width,
                "height": height
            }
        ]
    }
    response = requests.post(url="http://api.cdek.ru/calculator/calculate_tarifflist.php", headers=header, json=body).json()
    return response