def collect_cars(n: int):
    cars = {}
    for _ in range(n):
        car, mileage, fuel = input().split('|')
        cars[car] = {'Mileage': int(mileage), 'Fuel': int(fuel)}
    return cars


def collect_commands():
    commands = []

    while True:
        command = input()
        if command == 'Stop':
            break
        else:
            commands.append(command)
    return commands


def drive(data:list, cars: dict):
    car, distance, fuel = data[0], int(data[1]), int(data[2])
    if cars[car]['Fuel'] < fuel:
        print('Not enough fuel to make that ride')
    else:
        cars[car]['Mileage'] += distance
        cars[car]['Fuel'] -= fuel
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
    if cars[car]['Mileage'] >= 100000:
        print(f'Time to sell the {car}!')
        del cars[car]
    return cars


def refuel(data, cars):

    car, fuel = data[0], int(data[1])
    liters_to_full = 75 - cars[car]['Fuel']
    if fuel > liters_to_full:
        print(f'{car} refueled with {liters_to_full} liters')
        cars[car]['Fuel'] = 75
    else:
        print(f'{car} refueled with {fuel} liters')
        cars[car]['Fuel'] += fuel

    return cars


def revert(data, cars):
    car, kilometers = data[0], int(data[1])
    cars[car]['Mileage'] -= kilometers

    if cars[car]['Mileage'] <= 10000:
        cars[car]['Mileage'] = 10000
    else:
        print(f'{car} mileage decreased by {kilometers} kilometers')
    return cars


def process_commands(commands: list, cars: dict):

    for command in commands:
        action, *data = command.split(' : ')
        # data = command.split(' : ')
        if action == 'Drive':
            cars = drive(data, cars)
        elif action == 'Refuel':
            cars = refuel(data, cars)
        elif action == 'Revert':
            cars = revert(data, cars)

    return cars


number_of_cars = int(input())
car_collection = collect_cars(number_of_cars)
commands = collect_commands()
car_collection = process_commands(commands, car_collection)

for car, car_data in car_collection.items():
    print(f"{car} -> Mileage: {car_data['Mileage']} kms, Fuel in the tank: {car_data['Fuel']} lt.")
