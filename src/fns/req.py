import requests
import json
from typing import Callable

def create_request(func: Callable, **kwargs):

    url = f'https://api-fns.ru/api/{func.__name__}'

    try:
        response = requests.get(url=url, params=kwargs)

        if response.status_code == 200:
            try:
                json_data = response.json()
                return json_data
            except requests.exceptions.JSONDecodeError as e:
                raise f"JSON Decode Error: {e}\nResponse content: {response.text}"
            except TypeError as e:
                raise f"JSON Decode Error: {e}\nResponse content: {response.text}"
    except requests.exceptions.RequestException as e:
        raise f"An error occurred: {e}"
