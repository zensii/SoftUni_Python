prices = {
    "Large" : [16, 12, 9],
    "Medium": [13, 9, 7],
    "Small" : [9, 8, 5]
         }
size = input()
color = input()
orders = int(input())

production_cost = 0.35

index = {'Red': 0, 'Green': 1, 'Yellow': 2}[color]

price = orders * prices[size][index] * (1 - production_cost)
print(f'{price:.2f} leva.')
