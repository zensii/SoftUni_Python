budget = float(input())
season = input()

car_type = ''
clas = ''
price = 0

if budget <= 100:
    clas = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.65
elif 100 < budget <= 500:
    clas = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.8
else:
    clas = 'Luxury class'
    car_type = 'Jeep'
    price = budget * 0.9

print(f'{clas}')
print(f'{car_type} - {price:.2f}')
