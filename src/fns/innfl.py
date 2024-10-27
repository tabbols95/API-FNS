from src.fns.req import get_fns_data
from src.fns.req import FNSResponse
import re


def innfl(surname: str,
          name: str,
          patronymic: str,
          birth_date: str,
          type_document: str,
          number_document: str) -> FNSResponse:
    """Возвращает ИНН физического лица на основании введенных паспортных данных.

    Args:
        surname:
            Фамилия.
        name:
            Имя.
        patronymic:
            Отчетство.
        birth_date:
            Дата рождения в формате ДД.ММ.ГГГГ.
        type_document:
            Вид документа, удостоверяющего личность:
                01 - Паспорт гражданина СССР
                03 - Свидетельство о рождении
                10 - Паспорт иностранного гражданина
                12 - Вид на жительство в Российской Федерации
                15 - Разрешение на временное проживание в Российской Федерации
                19 - Свидетельство о предоставлении временного убежища на территории Российской Федерации
                21 - Паспорт гражданина Российской Федерации
                23 - Свидетельство о рождении, выданное уполномоченным органом иностранного государства
        number_document:
            Серия и номер документа (можно вводить как с пробелами, так и без пробелов между серией и номером).

    Returns:
        (FNSResponse)
    """
    pattern = re.compile('\\d{2}.\\d{2}.\\d{4}')
    if not surname or not name or not birth_date or not type_document or not number_document or not re.match(pattern, birth_date):
        answer = FNSResponse(method=innfl.__name__, error_flag=True, error_message='Error: values incorrect.')
        return answer

    return get_fns_data(innfl,
                        fam=surname,
                        nam=name,
                        otch=patronymic or 'нет',
                        bdate=birth_date,
                        doctype=type_document,
                        docno=number_document,
                        key='API_TOKEN')
