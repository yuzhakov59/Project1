import json
import logging
import os


logger = logging.getLogger('utilsLogger')
logger.setLevel(logging.DEBUG)  # Записываем всё
file_handler = logging.FileHandler('../logs/utils.log', 'w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
log_format = logging.Formatter('%(asctime)s – %(name)s – %(levelname)s – %(message)s', datefmt='%H:%M:%S')
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)


def transactions_from_json(file_path):
    """
    Принимает данные о финансовых транзакциях из JSON-файла.
    возвращает список в пайтон формате.
    """
    logger.info(f"Начинается обработка файла: {file_path}")
    try:
        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            logger.warning(f"Файл не найден: {file_path}")
            return []

        # Открываем файл для чтения
        with open(file_path, 'r', encoding="utf-8") as f:
            logger.info(f"Файл {file_path} успешно открыт.")
            try:
                # Загружаем JSON данные
                data = json.load(f)
                logger.info(f"JSON данные успешно загружены из файла {file_path}.")

                # Проверяем, является ли загруженные данные списком
                if isinstance(data, list):
                    logger.info("JSON данные являются списком.")
                    return data
                else:
                    logger.warning("Данные не являются списком. Возвращаем пустой список.")
                    return []
            except json.JSONDecodeError as e:
                # Обрабатываем ошибку, если файл содержит невалидный JSON
                logger.error(f"Ошибка декодирования JSON в {file_path}: {e}")
                return []
    except Exception as e:
        # Обрабатываем все остальные возможные ошибки
        logger.error(f"Непредвиденная ошибка при обработке {file_path}: {e}")
        return []
    finally:
        logger.info(f"Обработка файла {file_path} завершена.")


print(transactions_from_json('../data/operations.json'))
