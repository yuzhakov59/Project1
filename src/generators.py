def filter_by_currency(transactions, currency):
    while True:
        for y in transactions:
            if y["operationAmount"]["currency"]["name"] == currency:
                yield y
