from src.fns.req import create_request
import json


def egr(value: str):
    """Возвращает данные о компании.

    Args:
        value:
            ОГРН или ИНН искомой компании (юридического лица или ИП).

    Returns:
        list: Информация об искомой компании.
    """
    if not value:
        return []

    return create_request(egr, req=value, key='TOKEN')


if __name__ == "__main__":
    response = egr('1032502271548')
    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(response, json_file, ensure_ascii=False, indent=4)
