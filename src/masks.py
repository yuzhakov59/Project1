import logging
from typing import Union


logger = logging.getLogger('masksLogger')
logger.setLevel(logging.DEBUG)  # Записываем всё
file_handler = logging.FileHandler('../logs/masks.log', 'w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
log_format = logging.Formatter('%(asctime)s – %(name)s – %(levelname)s – %(message)s', datefmt='%H:%M:%S')
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str] = "0") -> str:
    """Функцию маскировки номера банковской карты"""
    logger.debug(f"Входящий номер карты: {card_number}")
    if card_number == "0":
        logger.warning("Номер карты не предоставлен.")
        return "Введите номер карты"
    elif len(card_number) == 16:
        logger.info("Номер карты замаскирован")
        return f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    else:
        logger.error("Введен некорректный номер карты.")
        return "Некорректно введён номер карты"


def get_mask_account(number_account: Union[str] = "0") -> str:
    """Функцию маскировки номера банковского счета"""
    logger.debug(f"Входящий номер счета: {number_account}")
    if len(number_account) == 20:
        logger.info("Номер счета замаскирован")
        return f"**{number_account[-4:]}"
    elif number_account == "0":
        logger.warning("Номер счета не предоставлен.")
        return "Введите номер счета"
    else:
        logger.error("Введен некорректный номер счета.")
        return "Некорректно введён номер счета"
