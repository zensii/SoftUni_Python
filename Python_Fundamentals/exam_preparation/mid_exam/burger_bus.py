number_of_cities = int(input())
total_profit = 0

for city_number in range(1, number_of_cities + 1):

    city_name = input()
    income = float(input())
    expenses = float(input())
    rainy_day_loss = 1

    if city_number % 3 == 0 and city_number % 5 != 0:
        expenses *= 1.5
    if city_number % 5 == 0:
        rainy_day_loss = 0.9

    profit = (income * rainy_day_loss) - expenses

    total_profit += profit

    print(f'In {city_name} Burger Bus earned {profit:.2f} leva.')

print(f'Burger Bus total profit: {total_profit:.2f} leva.')

