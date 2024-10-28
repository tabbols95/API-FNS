import requests
from datetime import datetime as dt
from typing import Callable, Optional, List
from dataclasses import dataclass


@dataclass
class FNSResponse:
    """Ответ по запросу"""

    method: str
    """Метод API ФНС"""

    url: str = f'https://api-fns.ru/api'
    """URL адрес"""

    status_code: Optional[int] = None
    """Код статуса ответа"""

    status: Optional[str] = None
    """Сообщение со статусом ответа"""

    encoding: str = 'utf-8'
    """Кодировка"""

    result: List[dict, None] = None
    """Ответ от сервиса"""

    error_flag: bool = False
    """Флаг ошибки"""

    error_message: Optional[str] = None
    """Сообщение об ошибке"""

    runtime: Optional[int] = None
    """Время получения ответа в секундах"""

    def get_url(self) -> str:
        full_url = self.url + '/' + self.method
        return full_url


def get_fns_data(func: Callable, **kwargs) -> FNSResponse:

    answer = FNSResponse(method=func.__name__)
    url = answer.get_url()

    try:
        start_dt = dt.now()
        response = requests.get(url=url, params=kwargs)
        end_dt = dt.now()
        answer.runtime = (end_dt - start_dt).total_seconds()

        # Записываем ответ
        answer.status_code = response.status_code
        answer.status = response.reason
        answer.encoding = response.encoding

        if response.status_code == 200:
            try:
                json_data = response.json()
                answer.result = json_data.get('items', [])
            except requests.exceptions.JSONDecodeError as e:
                answer.error_flag = True
                answer.error_message = f'JSONDecodeError: {e}.'
        else:
            answer.error_flag = True
            answer.error_message = f'Error: {response.status_code}.'
    except requests.exceptions.RequestException as e:
        # Записываем ответ об ошибке
        answer.error_flag = True
        answer.error_message = f'RequestException: {e}.'
    return answer
