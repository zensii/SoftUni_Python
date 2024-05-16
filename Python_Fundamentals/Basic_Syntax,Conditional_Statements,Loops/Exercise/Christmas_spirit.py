decoration_qty = int(input())
days_left = int(input())
total_cost = 0
spirit = 0

for day in range(1, days_left+1):
    if day % 11 == 0:
        decoration_qty += 2
    if day % 2 == 0:
        total_cost += 2 * decoration_qty
        spirit += 5
    if day % 3 == 0:
        total_cost += ((5 * decoration_qty) + (3 * decoration_qty))
        spirit += 13
    if day % 5 == 0:
        total_cost += 15 * decoration_qty
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_cost += (3 + 5 + 15)
if days_left % 10 == 0:
    spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit}')

