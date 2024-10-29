from inspect import getfullargspec
from itertools import chain
import requests
from typing import Callable, Any, Dict


BASE_URL = 'https://api-fns.ru/api'


class FnsResponseError(Exception):
    """Ошибка ответа о получении данных по API ФНС."""

    def __init__(self,
                 function: Callable[..., Any],
                 arg_dict: Dict[str, Any],
                 message: str = ""):
        if message:
            self.message = message
        self.func = function
        self.__dict__.update(arg_dict)

    def __repr__(self):
        return (
            f"FnsResponseError(func={self.func.__name__}, "
            f"args={({k: v for (k, v) in self.__dict__.items() if k != 'func'})})"
        )

    def __str__(self):
        return repr(self)


def func_args_as_dict(func: Callable[..., Any], *args, **kwargs):
    return dict(list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), args))
          + list(kwargs.items()))


def get_fns_data(func: Callable[..., Any], *args, **kwargs):
    """Получение данных по API ФНС."""

    url = f"{BASE_URL}/{func.__name__}"

    try:
        response = requests.get(url=url, params=kwargs)

        if response.status_code == 200:
            try:
                json_data = response.json()
                return json_data
            except requests.exceptions.JSONDecodeError as exp:
                return FnsResponseError(func, func_args_as_dict(func, *args, **kwargs), f"{exp}")
        else:
            return FnsResponseError(func, func_args_as_dict(func, *args, **kwargs), f"status code: {response.status_code}")
    except requests.exceptions.RequestException as exp:
        return FnsResponseError(func, func_args_as_dict(func, *args, **kwargs), f"{exp}")
