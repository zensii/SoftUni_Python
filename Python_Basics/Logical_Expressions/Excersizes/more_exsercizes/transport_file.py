n = int(input())
time = input()
taxi = 0
bus = 0
train = 0

if time == 'day':
    taxi = 0.70 + n * 0.79
elif time == 'night':
    taxi = 0.70 + n * 0.9

if n >= 20:
    bus = n * 0.09

if n >= 100:
    train = n * 0.06

if n < 20:
    print(f'{taxi:.2f}')
elif 20 <= n < 100:
    if taxi > bus:
        print(f'{bus:.2f}')
    else:
        print(f'{taxi:.2f}')
elif n >= 100:
    if taxi > bus:
        if bus > train:
            print(f'{train:.2f}')
        else:
            print(f'{bus:.2f}')
    elif taxi > train:
        print(f'{train:.2f}')
    else:
        print(f'{taxi:.2f}')
