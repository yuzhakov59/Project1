from typing import Union


def get_mask_card_number(card_number: Union[int]) -> str:
    """Функцию маскировки номера банковской карты"""

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(number_account: Union[int]) -> str:
    """Функцию маскировки номера банковского счета"""

    return f"**{number_account[-4:]}"
