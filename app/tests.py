import os

import requests


BASE_URL = 'http://localhost:5000'


def test_index():
    response = requests.get(BASE_URL, '/')
    assert response.content.decode('utf-8') == 'Hello, This is DaEun Kim.'


def test_info():
    response = requests.get(os.path.join(BASE_URL, 'info'))
    assert response.content.decode('utf-8') == 'Info'
