"""Method innfl."""

# local
from src.fns.req import get_fns_data
from validators import validator_innfl


@validator_innfl
def innfl(API_TOKEN: str,
          surname: str,
          name: str,
          patronymic: str,
          birth_date: str,
          type_document: str,
          number_document: str):
    """Возвращает ИНН физического лица на основании введенных паспортных данных.

    Args:
        API_TOKEN:
            Токен для подключения к API ФНС.
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

    return get_fns_data(innfl,
                        fam=surname,
                        nam=name,
                        otch=patronymic or 'нет',
                        bdate=birth_date,
                        doctype=type_document,
                        docno=number_document,
                        key=API_TOKEN)
