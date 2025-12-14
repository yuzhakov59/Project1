import os

from dotenv import load_dotenv

import unittest

from unittest.mock import patch

from src.external_api import rub_amount, currency_conversion

load_dotenv()
API_KEY = os.getenv('API_KEY')


@patch('requests.get')
def test_currency_conversion(mock_get):
    # Подготовка данных для мокирования ответа API
    mock_response = unittest.mock.Mock()
    mock_response.json.return_value = {'success': True, 'result': 75.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = currency_conversion(API_KEY, 'USD', 1)

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1",
        headers={"apikey": API_KEY}
    )
    assert result == 75.0


def test_rub_amount():
    assert rub_amount({
        "id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"
    }) == '31957.58'
