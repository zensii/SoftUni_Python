vacation_cost = float(input())
available_funds = float(input())
spend_counter = 0
days_counter = 0

while True:
    action = input()
    amount = float(input())
    if action == 'spend':
        available_funds -= amount
        if available_funds < 0:
            available_funds = 0
        spend_counter += 1
        days_counter += 1
        if spend_counter == 5:
            print("You can't save the money.")
            print(days_counter)
            break

    else:
        available_funds += amount
        days_counter += 1
        spend_counter = 0
        if available_funds >= vacation_cost:
            print(f'You saved the money for {days_counter} days.')
            break
