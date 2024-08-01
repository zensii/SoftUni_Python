cities = {}

while True:
    city = input()
    if city == 'Sail':
        break
    city, population, gold = city.split('||')

    if city not in cities:
        cities[city] = {'ppl': int(population), 'gold': int(gold)}
    else:
        cities[city]['ppl'] += int(population)
        cities[city]['gold'] += int(gold)

while True:
    command = input()
    if command == 'End':
        break

    action, *parameters = command.split('=>')

    if action == 'Plunder':
        town, people, gold = parameters
        cities[town]['ppl'] -= int(people)
        cities[town]['gold'] -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]['ppl'] == 0 or cities[town]['gold'] == 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif action == 'Prosper':
        town, gold = parameters
        if int(gold) < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[town]['gold'] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, city_stats in cities.items():
        print(f"{city} -> Population: {city_stats['ppl']} citizens, Gold: {city_stats['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
