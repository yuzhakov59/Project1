from typing import Union

from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card: Union[str]) -> str:
    """Функция принимает один аргумент — строку, возвращает строку с замаскированным номером"""

    account = "Счет"
    if account in account_card:
        return get_mask_account(account_card)
    else:
        return get_mask_card_number(account_card)


def get_date(date_format: Union[str]) -> str:
    """Функция преобразует дату"""

    return f'{date_format[8:10]}.{date_format[5:7]}.{date_format[0:4]}'
