days = 1
start_height = 5364
current_height = 5364
target_height = 8848
outcome = False

while not outcome:
    user_input = input()

    if user_input == 'END':
        print(f'Failed!')
        print(current_height)
        outcome = True
        break
    else:
        decision = user_input
        meters_gained = int(input())

    if decision == 'Yes':
        days += 1

    if days > 5:
        print(f'Failed!')
        print(current_height)
        outcome = True
        break

    current_height += meters_gained

    if current_height >= target_height:
        print(f'Goal reached for {days} days!')
        outcome = True
        break
