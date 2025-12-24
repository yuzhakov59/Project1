import csv
import openpyxl

from src.proba import result


def transactions_csv(file_csv):
    """
        функция считывания финансовых операций из CSV-файла,
        с выводом их в список словарей.
        """

    transactions = []
    try:
        with open(file_csv, mode='r', encoding='utf-8') as csvfile:
            # Итерируемся по каждой строке в CSV-файле
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                transactions.append(row)

    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути: {file_csv}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

    return transactions


def transactions_excel_xlsx(file_xlsx):
    """
            функция считывания финансовых операций из xlsx-файла,
            с выводом их в список словарей.
            """

    transactions = []
    try:
        # Открываем XLSX файл для чтения
        workbook = openpyxl.load_workbook(file_xlsx)

        # Получаем активный лист (обычно первый лист)
        sheet = workbook.active

        # Получаем заголовки столбцов из первой строки
        header = [cell.value for cell in sheet[1]]

        # Итерируемся по строкам, начиная со второй (чтобы пропустить заголовки)
        for row_num in range(2, sheet.max_row + 1):
            row = sheet[row_num]
            transaction = {}
            for i, cell in enumerate(row):
                transaction[header[i]] = cell.value
            transactions.append(transaction)

    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути: {file_xlsx}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

    return transactions
