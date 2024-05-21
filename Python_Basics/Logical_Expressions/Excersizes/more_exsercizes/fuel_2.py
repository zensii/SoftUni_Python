fuel_type = input()
liters = float(input())
discount_card = input()

gas = 222
diesel = 233
LPG = 93
discount_gas = 0
discount_diesel = 0
discount_LPG = 0
total_discount = 0

if discount_card == 'Yes':
    discount_gas = 18
    discount_diesel = 12
    discount_LPG = 8

if 20 <= liters <= 25:
    total_discount = 0.08
elif liters > 25:
    total_discount = 0.1

if fuel_type == 'Gasoline':
    price = ((gas - discount_gas) * liters) * (1 - total_discount)
    print(f'{price / 100:.2f} lv.')

elif fuel_type == 'Diesel':
    price = ((diesel - discount_diesel) * liters) * (1 - total_discount)
    print(f'{price / 100:.2f} lv.')

elif fuel_type == 'Gas':
    price = ((LPG - discount_LPG) * liters) * (1 - total_discount)
    print(f'{price / 100:.2f} lv.')
