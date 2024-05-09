M = int(input())
counter = 0
password = ''
first_combination = True

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a*b + c*d == M and a < b and c > d:
                    if not first_combination:
                        print(f' {a}{b}{c}{d}', end='')
                    else:
                        first_combination = False
                        print(f'{a}{b}{c}{d}', end='')
                    counter += 1
                    if counter == 4:
                        password = f'{a}{b}{c}{d}'

if password != '':
    print(f'\nPassword: {password}')
else:
    print('\nNo!')







