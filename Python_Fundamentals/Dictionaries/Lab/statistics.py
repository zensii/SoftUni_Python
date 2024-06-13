command = input()
inventory = {}

while True:
    if command == 'statistics':
        break

    item = command.split(': ')

    key = item[0]
    value = int(item[1])
    if key not in inventory:
        inventory[key] = value
    else:
        inventory[key] += value
    command = input()

print('Products in stock:')
for key, value in inventory.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(inventory.keys())}')
print(f'Total Quantity: {sum(inventory.values())}')
