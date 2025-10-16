import re
from typing import Union

def get_mask_card_number(card_number: Union[int]) -> str:
    """Функцию маскировки номера банковской карты"""

    record_type = ''.join(re.split('[^a-zA-Z]*', card_number))
    return f"record_type {card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(number_account: Union[int]) -> str:
    """Функцию маскировки номера банковского счета"""

    record_type = ''.join(re.split('[^a-zA-Z]*', number_account))
    return f"record_type **{number_account[-4:]}"
