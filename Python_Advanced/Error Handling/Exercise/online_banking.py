class MoneyNotEnoughError(Exception):
    """Insufficient funds for the requested transaction"""
    pass

class PINCodeError(Exception):
    """Invalid PIN code"""
    pass

class UnderageTransactionError(Exception):
    """You must be 18 years or older to perform online transactions"""
    pass

class MoneyIsNegativeError(Exception):
    """The amount of money cannot be a negative number"""
    pass


def send_money(cur_parameters: list, cur_balance: int) -> None:
    amount, pin = int(cur_parameters[0]), int(cur_parameters[1])

    if amount >= cur_balance:
        raise MoneyNotEnoughError(MoneyNotEnoughError.__doc__)
    if pin != pin_code:
        raise PINCodeError(PINCodeError.__doc__)
    if age < 18:
        raise UnderageTransactionError(UnderageTransactionError.__doc__)

    cur_balance -= amount
    print(f"Successfully sent {amount:.2f} money to a friend")
    print(f"There is {cur_balance:.2f} money left in the bank account")


def receive_money(cur_parameters: list, cur_balance: int) -> None:
    money = int(cur_parameters[0])

    if money < 0:
        raise MoneyIsNegativeError(MoneyIsNegativeError.__doc__)

    to_account_amount = money / 2
    cur_balance += to_account_amount
    print(f"{to_account_amount:.2f} money went straight into the bank account")


pin_code, balance, age = list(map(int, input().split(', ')))

while True:
    command = input()
    if command == 'End':
        break

    transaction, *parameters = command.split('#')

    if transaction == 'Send Money':
        send_money(parameters, balance)

    if transaction == 'Receive Money':
        receive_money(parameters, balance)
