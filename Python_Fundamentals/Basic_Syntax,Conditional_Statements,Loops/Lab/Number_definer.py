num = float(input())
addition = ''

if 0 < abs(num) < 1:
    addition = 'small'
elif abs(num) > 1000000:
    addition = 'large'

if num == 0:
    print('zero')
elif num > 0:
    print(f'{addition} positive')
else:
    print(f'{addition} negative')

