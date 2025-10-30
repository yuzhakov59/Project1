from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number() == "Введите номер карты"
    assert get_mask_card_number('70004567925289606361') == "Некорректно введён номер карты"
    assert get_mask_card_number('70007606361') == "Некорректно введён номер карты"

def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account() == "Введите номер счета"
    assert get_mask_account('736535874305') == "Некорректно введён номер счета"
    assert get_mask_account('73654108430148657467486535874305') == "Некорректно введён номер счета"