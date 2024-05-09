command = input()
total_steps = 0

while command != 'Going home':

    steps = int(command)
    total_steps += steps
    if total_steps >= 10000:
        print(f'Goal reached! Good job!')
        print(f'{total_steps - 10000} steps over the goal!')
        break
    command = input()

else:
    steps = int(input())
    total_steps += steps
    if total_steps < 10000:
        print(f'{10000 - total_steps} more steps to reach goal.')
    else:
        print('Goal reached! Good job!')
        print(f'{total_steps - 10000} steps over the goal!')
