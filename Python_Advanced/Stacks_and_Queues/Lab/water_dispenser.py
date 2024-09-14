from collections import deque

water_l = int(input())
names = deque()

while True:
    ppl = input()
    if ppl == 'Start':
        break
    names.append(ppl)

while True:
    commands = []
    command = input()
    if command == 'End':
        print(f'{water_l} liters left')
        break
    elif 'refill' in command:
        water_l += int(command.split()[1])
    else:
        drink = int(command)
        if drink <= water_l:
            water_l -= drink
            print(f'{names.popleft()} got water')
        else:
            print(f'{names.popleft()} must wait')


