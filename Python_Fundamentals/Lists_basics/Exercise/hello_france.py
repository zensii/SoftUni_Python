item_price_list = input().split('|')
initial_budget = float(input())
budget = initial_budget
buying_prices = []
selling_prices = []
total_gain = 0
string_prices = ''

for pairs in item_price_list:
    pair = pairs.split('->')

    if float(pair[1]) <= budget:
        if (pair[0] == 'Clothes' and float(pair[1]) <= 50.00 or pair[0] == 'Shoes' and float(pair[1]) <= 35.00 or
                pair[0] == 'Accessories' and float(pair[1]) <= 20.50):
            budget -= float(pair[1])
            buying_prices.append(pair[1])

    selling_prices = [(float(price) * 1.4) for price in buying_prices]
    total_gain = sum([float(price) for price in buying_prices])

for price in selling_prices:
    print(f'{float(price):.2f}', end=' ')

profit = sum(selling_prices) - (initial_budget - budget)
print(f'\nProfit: {profit:.2f}')

if sum(selling_prices) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')

