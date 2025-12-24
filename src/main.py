from src.utils import transactions_from_json
from src.transaction_filter import process_bank_search, process_bank_code
from src.table import transactions_csv, transactions_excel_xlsx
from src.processing import sort_by_date, filter_by_state


def operation_status(transaction):
    while True:
        stat = input('Введите статус, по которому необходимо выполнить фильтрацию. '
                       'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ')
        if (stat).lower() in "executed, canceled, pending":
            list_dict = transaction
            result = filter_by_state(list_dict, (stat).lower())
            print(f'Операции отфильтрованы по статусу "{stat}"')
            break
        else:
            print(f'Статус операции "{stat}" недоступен.')
    return result


def filter(transactions):
    sort_data = input('Отсортировать операции по дате? Да/Нет ')
    if (sort_data).lower() == 'да':
        filter_data = sort_by_date(transactions, reverse=True)
    else:
        filter_data = sort_by_date(transactions, reverse=False)

    sort_order = input('Отсортировать по возрастанию/по убыванию? ')
    if (sort_order).lower() == 'по возрастанию':
        filter_order = sorted(filter_data, key=lambda x: float(x["operationAmount"]["amount"]))
    else:
        filter_order = sorted(filter_data, key=lambda x: float(x["operationAmount"]["amount"]), reverse=True)

    sort_code = input('Выводить только рублевые транзакции? Да/Нет ')
    if (sort_code).lower() == 'да':
        filter_code = process_bank_code(filter_order)
    else:
        filter_code = filter_order

    sort_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет ')
    if (sort_word).lower() == 'да':
        filter_word = process_bank_search(filter_code)
    else:
        filter_word = filter_code

    return filter_word


def main():
    print("""Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
           """
          )
    customer_input = input('Введите порядковый номер операции ')
    if int(customer_input) == 1:
        print('Для обработки выбран JSON-файл.')
        file_path = ('../data/operations.json')
        transaction = transactions_from_json(file_path)
        transactions = operation_status(transaction)

    elif int(customer_input) == 2:
        print('Для обработки выбран CSV-файл.')
        status = operation_status()
        file_csv = ('../data/transactions.csv')
        transaction = transactions_csv(file_csv)
        transactions = operation_status(transaction)

    elif int(customer_input) == 3:
        print('Для обработки выбран XLSX-файл1.')
        status = operation_status()
        file_xlsx = ('../data/transactions_excel.xlsx')
        transaction = transactions_excel_xlsx(file_xlsx)
        transactions = operation_status(transaction)

    else:
        print('Введен неверный номер')

    result = filter(transactions)
    print(result)
    return result



if __name__ == "__main__": main()
