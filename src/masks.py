from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функцию маскировки номера банковской карты"""

    return f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(number_account: Union[str]) -> str:
    """Функцию маскировки номера банковского счета"""

    return f"**{number_account[-4:]}"
