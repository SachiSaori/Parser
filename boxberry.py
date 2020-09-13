# -*- coding: utf-8 -*-
import requests


height = length = width = "10"
weight = "1.5"


def get_city_id(kladr):
    response = requests.get("https://api.boxberry.ru/json.php?token=d6f33e419c16131e5325cbd84d5d6000&method=ListCitiesFull&CountryCode=643").json()
    for city in response:
        if city["Kladr"] == kladr:
            return city["Code"]


def get_delivery_points(sender_city_id, receiver_city_id):
    url = f'https://api.boxberry.ru/json.php?token=d6f33e419c16131e5325cbd84d5d6000&method=ListPointsShort&CountryCode=643&CityCode={sender_city_id}'
    sender_points = requests.get(url=url).json()
    url = f'https://api.boxberry.ru/json.php?token=d6f33e419c16131e5325cbd84d5d6000&method=ListPointsShort&CountryCode=643&CityCode={receiver_city_id}'
    receiver_points = requests.get(url=url).json()
    print(sender_points[0]["Code"], receiver_points[0]["Code"])
    return sender_points[0]["Code"], receiver_points[0]["Code"]


def calculate_delivery(sender_point, receiver_point):
    url = "https://api.boxberry.ru/json.php?token=d6f33e419c16131e5325cbd84d5d6000&method=DeliveryCosts"
    query = {
        "weight": weight,
        "height": height,
        "width": width,
        "depth": length,
        "targetstart": sender_point,
        "target": receiver_point,
        "ordersum": 0,
        "deliverysum": 0,
        "paysum": 1
    }
    response = requests.get(url=url, params=query).json()
    return response
