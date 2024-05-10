eggs_left = int(input())
total_sold = 0
eggs_order = 0

while True:
    user_input = input()

    if user_input == 'Close':
        print('Store is closed!')
        print(f'{total_sold} eggs sold.')
        break
    elif user_input == 'Fill':
        egg_fill = int(input())
        eggs_left += egg_fill

    elif user_input == 'Buy':
        eggs_order = int(input())

        if eggs_order <= eggs_left:
            total_sold += eggs_order
            eggs_left -= eggs_order

        else:
            print(f'Not enough eggs in store!')
            print(f'You can buy only {eggs_left}.')
            break




