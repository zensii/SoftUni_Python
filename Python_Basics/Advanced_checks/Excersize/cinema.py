type_movie = input()
row = int(input())
column = int(input())

price = 0

if type_movie == 'Premiere':
    price = 12
elif type_movie == 'Normal':
    price = 7.5
elif type_movie == 'Discount':
    price = 5

total = row * column * price

print(f'{total:.2f}')
