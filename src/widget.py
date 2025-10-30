import re


from typing import Union


from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: Union[str]) -> str:
    """Функция принимает один аргумент — строку, возвращает строку с замаскированным номером"""

    account = "Счет"
    cart_number = re.findall(r"\d+", account_card)[0]
    record_type = ''.join(re.split('[^a-zA-Zа-яА-Я ]*', account_card))
    if account in account_card:
        if len(cart_number) == 20:
            return f'{record_type}{get_mask_account(cart_number)}'
        else:
            return "Некорректно введён номер счета"
    else:
        if len(cart_number) == 16:
            return f'{record_type}{get_mask_card_number(cart_number)}'
        else:
            return "Некорректно введён номер карты"


def get_date(date_format: Union[str]) -> str:
    """Функция преобразует дату"""

    if len(date_format) == 26:
        return f'{date_format[8:10]}.{date_format[5:7]}.{date_format[0:4]}'
    else:
        return "Некорректно введёна дата"
