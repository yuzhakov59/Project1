from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    while True:
        for y in transactions:
            if not y:
                return "Нет транзакции"
            else:
                if y["operationAmount"]["currency"]["code"] == currency:
                    yield y


def transaction_descriptions(transactions: list[dict]) -> str:
    while True:
        for y in transactions:
            if not y:
                return "Нет транзакции"
            else:
                if "description" in y:
                    yield y["description"]


card_number_generator =