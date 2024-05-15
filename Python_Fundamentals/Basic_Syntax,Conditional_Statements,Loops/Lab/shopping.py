budget = int(input())

while True:
    user_input = input()
    if user_input == 'End':
        if budget >= 0:
            print('You bought everything needed.')
        break
    price = int(user_input)
    budget -= price
    if budget < 0:
        print('You went in overdraft!')
        break
