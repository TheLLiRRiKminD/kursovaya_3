import json


def read_json():
    with open("../operations.json", encoding="UTF-8") as file:
        transactions_data = json.load(file)
        return transactions_data


def mask_card_number(card_number):
    masked_number = "XXXX XX** **** " + card_number[-4:]
    return masked_number


def mask_account_number(account_number):
    masked_number = "**" + account_number[-4:]
    return masked_number


def print_last_5_operations(operations):
    executed_transactions = [transaction for transaction in operations if transaction.get("state", '') == 'EXECUTED']
    operations = sorted(executed_transactions, key=lambda x: x['date'], reverse=True)[:5]
    for operation in operations:
        date = operation['date'][:10]
        description = operation['description']
        from_account = mask_card_number(operation.get('from', ''))
        to_account = mask_account_number(operation.get('to', ''))
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['code']

        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}\n")


print_last_5_operations(read_json())