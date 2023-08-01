import json


def read_json():
    with open("operations.json", encoding="UTF-8") as file:
        transactions_data = json.load(file)
        return transactions_data


def print_last_5_transactions(transactions_data):
    # Фильтруем транзакции, оставляя только выполненные (state == "EXECUTED")
    executed_transactions = [transaction for transaction in transactions_data if transaction["state"] == 'EXECUTED']

    # Сортируем выполненные транзакции по дате в обратном порядке (по убыванию)
    sorted_transactions = sorted(executed_transactions, key=lambda x: x['date'], reverse=True)

    # Выводим информацию о последних 5 выполненных транзакциях
    for transaction in sorted_transactions[:5]:
        print_transaction(transaction)
        print('\n')

def print_transaction(transaction):
    print(f"{transaction['date']} {transaction['description']}")
    if 'from' in transaction:
        print(f"{transaction['from']} -> {transaction['to']}")
    else:
        print(f"Перевод на счет {transaction['to']}")
    print(f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")


print_last_5_transactions(read_json())