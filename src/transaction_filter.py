import re
from collections import Counter


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """
    Функция для поиска банковских операций по строке в описании.
    """

    results = []
    for transaction in data:
    # Получаем описание транзакции, приводим к нижнему регистру
        description = transaction.get('description').lower()
        search = search.lower()
        if re.search(r'\b' + re.escape(search) + r'\b', description):
            results.append(transaction)

    return results


def process_bank_operations(data:list[dict], categories:list)->dict:
    """
    Функция для подсчета банковских операций по строке в описании.
    """
    results = []
    new_categories = list(map(str.lower, categories))
    for transaction in data:
        description = transaction.get('description').lower()
        if description in new_categories:
            results.append(description)
        else:
            pass
    new_results = Counter(results)

    return new_results


def process_bank_code(data):
    """
    Функция для поиска рублёвых банковских операций в описании.
    """

    results = []
    code = 'RUB'
    for transaction in data:
        if transaction['operationAmount']['currency']['code'] == code:
            results.append(transaction)

    return results
