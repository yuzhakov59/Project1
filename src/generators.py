from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
    """

    for y in transactions:
        if y["operationAmount"]["currency"]["code"] == currency:
            yield y


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """
    Функция генератор который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """

    for y in transactions:
        if "description" in y:
            yield y["description"]


def card_number_generator(start: int, stop: int) -> Iterator:
    """
    Функция генератор который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
     от 0000 0000 0000 0001 до 9999 9999 9999 9999. Генератор должен принимать
     начальное и конечное значения для генерации диапазона номеров.
    """

    while True:
        try:
            if start < 0 or stop > 9999999999999999 or start >= stop:
                yield "Не верный диапазон."
        except StopIteration:
            break

        for num in range(start, stop + 1):
            num_str = f"{num:016d}"
            formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
            yield formatted_number
