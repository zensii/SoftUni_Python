def receive(command, food_list):
    quantity = int(command[1])
    food = command[2]
    if quantity > 0:
        food_list[food] = food_list.get(food, 0) + quantity
    return food_list


def sell(command, food_list):
    quantity = int(command[1])
    food = command[2]
    if food not in food_list:
        print(f'You do not have any {food}.')
    elif food_list[food] < quantity:
        print(f"There aren't enough {food}. You sold the last {food_list[food]} of them.")
        food_list['total sold'] += food_list[food]
        del food_list[food]
    else:
        food_list[food] -= quantity
        food_list['total sold'] += quantity
        print(f'You sold {quantity} {food}.')
        if food_list[food] == 0:
            del food_list[food]


def main():

    food_list = {'total sold': 0}
    usr_input = input()

    while usr_input != 'Complete':
        command = usr_input.split()

        if command[0] == 'Receive':
            receive(command, food_list)

        if command[0] == 'Sell':
            sell(command, food_list)

        usr_input = input()

    for food, quantity in food_list.items():
        if food != 'total sold':
            print(f'{food}: {quantity}')
    print(f"All sold: {food_list['total sold']} goods")


if __name__ == '__main__':
    main()
