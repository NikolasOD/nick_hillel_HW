import requests


def get_rates():
    response = requests.get('https://bitpay.com/api/rates')
    return response.json()
