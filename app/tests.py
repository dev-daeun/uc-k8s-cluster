import json
import os

import requests


BASE_URL = 'http://localhost:5000'


def test_index():
    response = requests.get(BASE_URL, '/')
    assert response.content.decode('utf-8') == 'Hello, This is DaEun Kim.'


def test_info():
    response = requests.get(os.path.join(BASE_URL, 'info'))
    assert json.loads(response.content.decode('utf-8')) == {
        'email': 'kde6260@gmail.com',
        'linked-in': 'https://www.linkedin.com/in/daeun-kim-156085183/',
        'github': 'https://github.com/dev-daeun',
    }
