def fire(index, damage):

    if 0 <= index < len(warship_status):
        warship_status[index] -= damage
        if warship_status[index] <= 0:
            print('You won! The enemy ship has sunken.')
            return True
    return False


def defend(start_index, end_index, damage):

    if 0 <= start_index <= end_index < len(ship_status):
        for section in range(start_index, end_index+1):
            ship_status[section] -= damage
            if ship_status[section] <= 0:
                print(f'You lost! The pirate ship has sunken.')
                return True
        return False


def repair(index, health):
    if 0 <= index < len(ship_status):
        ship_status[index] += health
        if ship_status[index] > max_section_health:
            ship_status[index] = max_section_health


def status():
    damaged_sections = 0
    for section in ship_status:
        if section < max_section_health * 0.2:
            damaged_sections += 1
    return damaged_sections


ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
max_section_health = int(input())
win = False
lose = False
command = input()

while command != 'Retire':

    action = command.split()

    if action[0] == 'Fire':
        win = fire(int(action[1]), int(action[2]))
    elif action[0] == 'Defend':
        lose = defend(int(action[1]), int(action[2]), int(action[3]))
    elif action[0] == 'Repair':
        repair(int(action[1]), int(action[2]))
    elif action[0] == 'Status':
        print(f'{status()} sections need repair.')

    if win or lose:
        break

    command = input()

else:
    print(f'Pirate ship status: {sum(ship_status)}')
    print(f'Warship status: {sum(warship_status)}')
