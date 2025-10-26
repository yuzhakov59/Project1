from typing import List, Dict

from datetime import datetime


def filter_by_state(list_dictionaries: List[Dict[str, str]], state = 'EXECUTED': [str]) -> List[Dict[str, str]]:
    """
    Функция принимает список словарей и опционально значение для ключа
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению.
    """

    list_dictionaries

    return


print(filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]))


def sort_by_date(banking_operation: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """
    Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате
    """

    return sorted(banking_operation, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)

banking_operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

sorted_operations = sort_by_date(banking_operations)
print(sorted_operations)