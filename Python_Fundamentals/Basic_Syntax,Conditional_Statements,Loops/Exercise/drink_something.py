index = 0
ages = [14, 18, 21]
category = ['toddy',
            'coke',
            'beer',
            'whisky'
            ]
age_input = int(input())

for age in ages:
    if age_input <= age:
        print(f'drink {category[index]}')
        break
    index += 1
else:
    print('drink whisky')
