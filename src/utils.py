import json
import time


def read_json():
    """Функция чтения JSON файла"""
    with open("../operations.json", encoding="UTF-8") as file:
        transactions_data = json.load(file)
        return transactions_data


def mask_card_number(card_number):
    info_about_card = card_number.split()
    if len(info_about_card) == 3:
        return f"{info_about_card[0]} {info_about_card[1]} {info_about_card[2][:4]} {info_about_card[2][4:6]}** **** {info_about_card[2][-4:]}"
    elif len(info_about_card) == 2:
        return f"{info_about_card[0]} {info_about_card[1][:4]} {info_about_card[1][4:6]}** **** {info_about_card[1][-4:]}"
    elif len(info_about_card) == 1:
        return f"{info_about_card[0][:4]} {info_about_card[0][4:6]}** **** {info_about_card[0][-4:]}"
    else:
        return ""


def mask_account_number(account_number):
    info_about_account = account_number.split()
    if len(info_about_account) == 3:
        return f"{info_about_account[0]} {info_about_account[1]} **{info_about_account[2][-4:]}"
    elif len(info_about_account) == 2:
        return f"{info_about_account[0]} **{info_about_account[1][-4:]}"
    elif len(info_about_account) == 1:
        return f"**{info_about_account[0][-4:]}"
    else:
        return ""


def print_last_5_operations(operations):
    executed_transactions = [transaction for transaction in operations if transaction.get("state", '') == 'EXECUTED']
    operations = sorted(executed_transactions, key=lambda x: x['date'], reverse=True)[:5]
    for operation in operations:
        date_ = time.strptime(operation['date'][:10], "%Y-%m-%d")
        date = time.strftime("%d.%m.%Y", date_)
        description = operation['description']
        from_account = mask_card_number(operation.get('from', ''))
        to_account = mask_account_number(operation.get('to', ''))
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        print(f"{date} {description}")
        if from_account == "":
            print(to_account)
        else:
            print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}\n")

if __name__ == "__main__":
    print_last_5_operations(read_json())