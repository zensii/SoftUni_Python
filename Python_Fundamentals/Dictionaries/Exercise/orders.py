# def add_products():
#     inventory = {}
#     while True:
#
#         product = input().split()
#
#         if len(product) == 1:
#
#             return inventory
#
#         product_name = product[0]
#         product_price = float(product[1])
#         product_quantity = int(product[2])
#
#         if product_name in inventory:
#
#             inventory[product_name][1] += product_quantity
#         else:
#             inventory[product_name] = [0.0, 0]
#
#             inventory[product_name][1] = product_quantity
#
#         inventory[product_name][0] = product_price
#
#
# def main():
#     inventory = add_products()
#     for item, info in inventory.items():
#         print(f'{item} -> {info[0] * info[1]:.2f}')
#
#
# if __name__ == '__main__':
#     main()
def add_products():
    inventory = {}

    while True:
        command = input()
        if command == 'buy':
            return inventory

        product_name, product_price, product_quantity = command.split()
        product_price = float(product_price)
        product_quantity = int(product_quantity)

        if product_name in inventory:
            inventory[product_name]['Quantity'] += product_quantity

        else:
            inventory[product_name] = {'Quantity': product_quantity}

        inventory[product_name]['Product_price'] = product_price


def main():
    inventory = add_products()
    for item, info in inventory.items():
        print(f'{item} -> {info['Product_price'] * info['Quantity']:.2f}')


if __name__ == '__main__':
    main()
