from src.fns.req import get_fns_data
from src.fns.req import FNSResponse


def egr(value: str) -> FNSResponse:
    """Возвращает данные о компании.

    Args:
        value:
            ОГРН или ИНН искомой компании (юридического лица или ИП).

    Returns:
        list: Информация об искомой компании.
    """
    if not value:
        answer = FNSResponse(method=egr.__name__)
        answer.error_flag = True
        answer.error_message = 'Error: value is None.'
        return answer

    return get_fns_data(egr, req=value, key='API_TOKEN')
