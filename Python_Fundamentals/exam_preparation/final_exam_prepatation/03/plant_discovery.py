def gather_data(n: int):
    plants = {}
    for inpt in range(n):
        plant, rarity = input().split('<->')
        plants[plant] = {'Rarity': rarity, 'Rating': []}
    return plants


def process_commands(commands: list, plants: dict):

    for command in commands:
        action, plant_rate = command.split(': ')

        if plant_rate.split()[0] not in plants:
            print('error')

        elif action == 'Rate':
            plant, rating = plant_rate.split(' - ')
            plants = rate(plant, int(rating), plants)

        elif action == 'Update':
            plant, new_rarity = plant_rate.split(' - ')
            plants = update(plant, int(new_rarity), plants)

        elif action == 'Reset':
            plant_reset = plant_rate
            plants = reset(plant_reset, plants)

    return plants


def rate(plant: str, rate: int, plants: dict):

    plants[plant]['Rating'].append(rate)

    return plants


def update(plant: str, new_rarity: int, plants: dict):

    plants[plant]['Rarity'] = new_rarity

    return plants


def reset(plant: str, plants: dict):
    plants[plant]['Rating'].clear()

    return plants


n = int(input())
plants = gather_data(n)
commands = []

while True:
    command = input()
    if command == 'Exhibition':
        break
    else:
        commands.append(command)

plants = process_commands(commands, plants)

print('Plants for the exhibition:')

for plant, plant_info in plants.items():
    plant_rarity, ratings = plant_info.values()

    if not ratings:
        rating = 0
    else:
        rating = sum(plant_info['Rating'])/len(plant_info['Rating'])

    print(f"- {plant}; Rarity: {plant_info['Rarity']}; Rating: {rating:.2f}")
