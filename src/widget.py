from typing import Union


def mask_account_card(account_card: Union[str]) -> str:
    """ Функция принимает один аргумент — строку, возвращает строку с замаскированным номером"""

    return


def get_date(date_format: Union[str]) -> str:
    """ Функция преобразует дату"""

    return f'"{date_format[9:11]}.{date_format[6:8]}.{date_format[1:5]}"'