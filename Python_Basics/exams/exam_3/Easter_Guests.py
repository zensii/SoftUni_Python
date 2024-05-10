import math

guests = int(input())
budget = int(input())

cakes = math.ceil(guests/3)
eggs = guests * 2
cake_price = 4
egg_price = 0.45

total_cost = eggs * egg_price + cakes * cake_price

if budget >= total_cost:
    print(f'Lyubo bought {cakes} Easter bread and {eggs} eggs.')
    print(f'He has {budget - total_cost:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f'He needs {abs(budget - total_cost):.2f} lv. more.')

