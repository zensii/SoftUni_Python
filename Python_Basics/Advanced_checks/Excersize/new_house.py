flower = input()
quantity = int(input())
budget = int(input())

# prices

rose_price = 5
dalia_price = 3.8
lale_price = 2.8
narcis_price = 3
gladiola_price = 2.5
discount = 0
total = 0

if flower == 'Roses':
    if quantity > 80:
        discount = 0.1
    total = rose_price * quantity * (1 - discount)

if flower == 'Dahlias':
    if quantity > 90:
        discount = 0.15
    total = dalia_price * quantity * (1 - discount)

if flower == 'Tulips':

    if quantity > 80:
        discount = 0.15
    total = lale_price * quantity * (1 - discount)

if flower == 'Narcissus':

    if quantity < 120:
        discount = -0.15
    total = narcis_price * quantity * (1 - discount)

if flower == 'Gladiolus':

    if quantity < 80:
        discount = -0.2
    total = gladiola_price * quantity * (1 - discount)

if budget >= total:
    print(f'Hey, you have a great garden with {quantity} {flower} and {budget - total:.2f} leva left.')
else:
    print(f'Not enough money, you need {total - budget:.2f} leva more.')
