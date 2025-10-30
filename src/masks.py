from typing import Union


def get_mask_card_number(card_number: Union[str] = '0') -> str:
    """Функцию маскировки номера банковской карты"""

    if card_number == '0':
        return "Введите номер карты"
    elif len(card_number) == 16:
        return f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    else:
        return "Некорректно введён номер карты"



def get_mask_account(number_account: Union[str] = '0') -> str:
    """Функцию маскировки номера банковского счета"""

    if len(number_account) == 20:
        return f"**{number_account[-4:]}"
    elif number_account == '0':
        return "Введите номер счета"
    else:
        return "Некорректно введён номер счета"

