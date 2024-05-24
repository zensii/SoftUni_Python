fires = input().split('#')
water = int(input())
effort = 0
total_fire = 0
put_out_fires = []

for fire in fires:
    type_fire = fire.split(' = ')

    if ((type_fire[0] == 'High' and 81 <= int(type_fire[1]) <= 125) or (type_fire[0] == 'Medium' and
            51 <= int(type_fire[1]) <= 80) or (type_fire[0] == 'Low' and 1 <= int(type_fire[1]) <= 50)):

        needed_water = int(type_fire[1])

        if needed_water <= water:
            water -= int(type_fire[1])
            effort += int(type_fire[1]) * 0.25
            total_fire += int(type_fire[1])
            put_out_fires.append(type_fire[1])
        else:
            continue

    else:
        continue

print('Cells:')

for fire in put_out_fires:
    print(f' - {fire}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
