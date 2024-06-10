energy = int(input())
command = input()
battles_won = 0

while command != 'End of battle':
    required_energy = int(command)
    if required_energy <= energy:
        energy -= required_energy
        battles_won += 1

        if battles_won % 3 == 0:
            energy += battles_won

    else:
        print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        break

    command = input()

else:
    print(f'Won battles: {battles_won}. Energy left: {energy}')
