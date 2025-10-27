from typing import List, Dict


from datetime import datetime


def filter_by_state(list_dict: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Функция принимает список словарей и опционально значение для ключа
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению.
    """

    new_list = []
    for i in list_dict:
        if i['state'] == state:
            new_list.append(i)
    return new_list


def sort_by_date(banking_operation: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """
    Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором словари отсортированы по дате
    """

    return sorted(banking_operation, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)
