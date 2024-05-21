n = int(input())
time = input()
taxi = 0
bus = 0
train = 0

if n < 20:
    if time == 'day':
        taxi = 0.70 + n * 0.79
    elif time == 'night':
        taxi = 0.70 + n * 0.9
    print(f'{taxi:.2f}')

elif 20 <= n < 100:
    bus = n * 0.09
    print(f'{bus:.2f}')

elif n >= 100:
    train = n * 0.06
    print(f'{train:.2f}')
