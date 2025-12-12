import json

import os


def transactions_from_json(file_path):
    """
    Принимает данные о финансовых транзакциях из JSON-файла.
    возвращает список в пайтон формате.
    """
    try:
        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            return []

        # Открываем файл для чтения
        with open(file_path, 'r', encoding="utf-8") as f:
            try:
                # Загружаем JSON данные
                data = json.load(f)

                # Проверяем, является ли загруженные данные списком
                if isinstance(data, list):
                    return data
                else:
                    return []
            except json.JSONDecodeError:
                # Обрабатываем ошибку, если файл содержит невалидный JSON
                return []
    except Exception as e:
        # Обрабатываем все остальные возможные ошибки
        print(f"Ошибка при чтении файла: {e}")
        return []
