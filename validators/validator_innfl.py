
# external
from functools import wraps
from typing import Callable, Any
import re

# local
from src.fns.req import FnsResponseError, func_args_as_dict


def validator_innfl(func: Callable[..., Any]):
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        pattern = re.compile('\\d{2}.\\d{2}.\\d{4}')
        try:
            if ((('surname' in kwargs and kwargs['surname']) or args[1]) and
                (('name' in kwargs and kwargs['name']) or args[2]) and
                (('birth_date' in kwargs and kwargs['birth_date'] and re.match(pattern, kwargs['birth_date'])) or
                 (args[4] and re.match(pattern, args[4]))) and
                (('type_document' in kwargs and kwargs['type_document']) or args[5]) and
                (('number_document' in kwargs and kwargs['number_document']) or args[6])
            ):
                return func(*args, **kwargs)
            else:
                return FnsResponseError(func, func_args_as_dict(func, *args, **kwargs), "Invalid data.")
        except Exception as exp:
            return FnsResponseError(func, func_args_as_dict(func, *args, **kwargs), f"{exp}")

    return wrapper
