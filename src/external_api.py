import requests

import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def currency_conversion(api_key, code, amount):
    """
    Конвертирует валюту в рубли, используя Exchange Rates Data API.
    """
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

    # Добавляем API ключ в заголовок запроса, как требует документация API.
    headers = {
        "apikey": api_key
    }

    try:
        # Отправляем GET запрос к API.
        response = requests.get(url, headers=headers)

        # Проверяем статус ответа. Если код не 200 (OK), вызываем исключение.
        response.raise_for_status()

        # Преобразуем JSON ответ в словарь Python.
        data = response.json()

        # Проверяем, был ли запрос к API успешным.
        if data.get('success'):
            return data['result']
        else:
            # Если неуспешно, печатаем сообщение об ошибке и возвращаем None.
            print(f"Ошибка API: {data.get('error', 'Неизвестная ошибка')}")
            return None

    except requests.exceptions.RequestException as e:
        # Обрабатываем ошибки, связанные с сетевым подключением.
        print(f"Ошибка подключения: {e}")
        return None


def rub_amount(transaction):
    """
    Конвертирует и выводит сумму транзакции в рублях.
    """

    amount = transaction['operationAmount']['amount']
    code = transaction['operationAmount']['currency']['code']

    if code == 'RUB':
        return amount
    elif code == 'USD':
        return currency_conversion(API_KEY, code, amount)
    elif code == 'EUR':
        return currency_conversion(API_KEY, code, amount)
    else:
        raise ValueError(f"Неподдерживаемая валюта: {code}")
