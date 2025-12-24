from src.transaction_filter import process_bank_search, process_bank_operations


def test_process_bank_search(transactions):
    search = 'Перевод организации'
    data = transactions
    assert process_bank_search(data, search) == [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]


def test_process_bank_operations(transactions):
    categories = ['Перевод организации']
    data = transactions
    assert process_bank_operations(data, categories) == {'перевод организации': 2}
