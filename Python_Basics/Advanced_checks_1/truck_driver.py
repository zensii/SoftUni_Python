season = input()
kilometers = float(input())
salary = 0

if kilometers <= 5000:
    if season == 'Spring' or season == 'Autumn':
        salary = 0.75 * kilometers
    elif season == 'Summer':
        salary = 0.9 * kilometers
    else:
        salary = 1.05 * kilometers
elif 5000 < kilometers <= 10000:
    if season == 'Spring' or season == 'Autumn':
        salary = 0.95 * kilometers
    elif season == 'Summer':
        salary = 1.1 * kilometers
    else:
        salary = 1.25 * kilometers
else:
    salary = 1.45 * kilometers

print(f'{(salary * 4) * 0.9:.2f}')


