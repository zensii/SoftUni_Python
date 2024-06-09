def order():
    order_price = 0
    brute_price = 0
    taxes = 0
    while True:

        user_input = input()

        try:
            part_price = float(user_input)
            if part_price < 0:
                print('Invalid price!')
                continue
            brute_price += part_price
            order_price += part_price * 1.2
            taxes += part_price * 0.2
        except ValueError:

            user_category = user_input
            order_price = order_price * user_type(user_category)
            break

    return order_price, brute_price, taxes


def user_type(user):
    discount = 1
    if user == 'special':
        discount = 0.9

    return discount


prices = order()

if prices[0] == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {prices[1]:.2f}$")
    print(f"Taxes: {prices[2]:.2f}$")
    print(f"-----------")
    print(f"Total price: {prices[0]:.2f}$")
