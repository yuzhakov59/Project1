from unittest.mock import mock_open, patch

from src.utils import transactions_from_json


# Создаем объект, который будет представлять замоканную версию функции open
mock_file = mock_open(read_data='[{"id": 441945886,"state": "EXECUTED"}]')


@patch('builtins.open', mock_file)
def test_transactions_from_json():
    with patch('json.load', return_value=[{"id": 441945886, "state": "EXECUTED"}]):
        assert transactions_from_json('./data/operations.json') == []
