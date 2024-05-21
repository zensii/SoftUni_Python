budget = float(input())
season = input()  # summer or winter

destination = ""
total = 0
housing = ''

if season == 'summer' and not budget > 1000:
    housing = 'Camp'
else:
    housing = 'Hotel'

if budget <= 100:
    destination = "Bulgaria"
    if season == 'summer':
        total = budget * 0.3
    else:
        total = budget * 0.7

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        total = budget * 0.4
    else:
        total = budget * 0.8

else:
    destination = 'Europe'
    if season == 'summer':
        total = budget * 0.9
    else:
        total = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{housing} - {total:.2f}')
