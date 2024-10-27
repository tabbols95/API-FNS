from src.fns.req import get_fns_data
from src.fns.req import FNSResponse


def nalogbi(inn: str) -> FNSResponse:
    """Возвращает данные о компании.

    Args:
        inn:
            ИНН искомой компании (юридического лица или ИП).

    Returns:
        list: Информация об искомой компании.
    """
    if not inn:
        answer = FNSResponse(method=nalogbi.__name__)
        answer.error_flag = True
        answer.error_message = 'Error: value is None.'
        return answer

    return get_fns_data(nalogbi, inn=inn, key='API_TOKEN')
