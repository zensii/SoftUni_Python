juniors = int(input())
seniors = int(input())
type_race = input()

donation = 0
price = 0

if type_race == 'trail':
    donation = juniors * 5.5 + seniors * 7
elif type_race == 'cross-country':
    if juniors + seniors >= 50:
        donation = juniors * (8 * 0.75) + seniors * (9.5 * 0.75)
    else:
        donation = juniors * 8 + seniors * 9.5
elif type_race == 'downhill':
    donation = juniors * 12.25 + seniors * 13.75
else:
    donation = juniors * 20 + seniors * 21.5

print(f'{donation * 0.95:.2f}')
