from src.fns.req import get_fns_data
from src.fns.req import AnswerRequest


def nalogbi(inn: str) -> AnswerRequest:
    """Возвращает данные о компании.

    Args:
        inn:
            ИНН искомой компании (юридического лица или ИП).

    Returns:
        list: Информация об искомой компании.
    """
    if not inn:
        answer = AnswerRequest(method=nalogbi.__name__)
        answer.error_flag = True
        answer.error_message = 'Error: value is None.'
        return answer

    return get_fns_data(nalogbi, inn=inn, key='API_TOKEN')
