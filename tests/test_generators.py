import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions, currency="USD"):
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


@pytest.mark.parametrize(
    "start, stop, x",
    [
        (1, 5, "0000 0000 0000 0001"),
        (546875, 54687545, "0000 0000 0054 6875"),
        (345678976, 3456789765, "0000 0003 4567 8976"),
        (65874589654587458, 658745896545874585, "Не верный диапазон."),
        (5, 1, "Не верный диапазон."),
    ],
)
def test_card_number_generator(start, stop, x):
    number_generator = card_number_generator(start, stop)
    assert next(number_generator) == x
