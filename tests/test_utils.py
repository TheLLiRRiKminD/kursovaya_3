import pytest
from src.utils import mask_card_number, mask_account_number, print_last_5_operations, read_json


def test_mask_card_number():
    assert mask_card_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_card_number("Master Card 7158300734726758") == "Master Card 7158 30** **** 6758"
    assert mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert mask_card_number("") == ""


def test_mask_account_number():
    assert mask_account_number("Master Card 64686473678894779589") == "Master Card **9589"
    assert mask_account_number("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_number("Счет 35383033474447895560") == "Счет **5560"
    assert mask_account_number("1234567890123456") == "**3456"
    assert mask_account_number("7890") == "**7890"
    assert mask_account_number("") == ""


def test_print_last_5_operations(capsys):
    test_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]

    print_last_5_operations(test_data)

    captured = capsys.readouterr()
    expected_output = (
        "26.08.2019 Перевод организации\n"
        "Maestro 1596 83** **** 5199 -> Счет **9589\n"
        "31957.58 руб.\n\n"
        "03.07.2019 Перевод организации\n"
        "MasterCard 7158 30** **** 6758 -> Счет **5560\n"
        "8221.37 USD\n\n"
        "04.04.2019 Перевод со счета на счет\n"
        "Счет 1970 86** **** 8542 -> Счет **4188\n"
        "79114.93 USD\n\n"
        "30.06.2018 Перевод организации\n"
        "Счет 7510 68** **** 6952 -> Счет **6702\n"
        "9824.07 USD\n\n"
        "23.03.2018 Открытие вклада\n"
        "Счет **2431\n"
        "48223.05 руб.\n\n"

    )
    assert captured.out == expected_output


def test_no_exceptions():
    try:
        print_last_5_operations(read_json())
    except Exception as e:
        pytest.fail(f"Function raised an exception: {e}")
