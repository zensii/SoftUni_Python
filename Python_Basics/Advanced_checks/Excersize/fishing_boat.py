budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter"
number = int(input())

total_price = 0
price = 0

if season == 'Spring':
    if number <= 6:
        price = 3000 * 0.9
    elif 7 <= number <= 11:
        price = 3000 * 0.85
    elif number >= 12:
        price = 3000 * 0.75

elif season == 'Summer' or season == 'Autumn':
    if number <= 6:
        price = 4200 * 0.9
    elif 7 <= number <= 11:
        price = 4200 * 0.85
    elif number >= 12:
        price = 4200 * 0.75

else:
    if number <= 6:
        price = 2600 * 0.9
    elif 7 <= number <= 11:
        price = 2600 * 0.85
    elif number >= 12:
        price = 2600 * 0.75

if number % 2 == 0 and not season == 'Autumn':
    total_price = price * 0.95
else:
    total_price = price

if total_price <= budget:
    print(f'Yes! You have {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva.')
