balance = 0

while True:

    text = input()
    if text == 'NoMoreMoney':
        break

    installment = float(text)

    if float(installment) < 0:
        print('Invalid operation!')
        break

    else:
        balance += installment
        print(f'Increase: {installment:.2f}')

print(f'Total: {balance:.2f}')
