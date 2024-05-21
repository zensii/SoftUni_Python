budget = float(input())
season = input()
housing = ''
location = ''
cost = 0

if season == 'Summer':
    location = 'Alaska'
else:
    location = ' Morocco'

if budget <= 1000:
    housing = 'Camp'
    if location == 'Alaska':
        cost = budget * 0.65
    else:
        cost = budget * 0.45

elif 1000 < budget <= 3000:
    housing = 'Hut'
    if location == 'Alaska':
        cost = budget * 0.8
    else:
        cost = budget * 0.6
else:
    housing = 'Hotel'
    cost = budget * 0.9

print(f'{location} - {housing} - {cost:.2f}')
