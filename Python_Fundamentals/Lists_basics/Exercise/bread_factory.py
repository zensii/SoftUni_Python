current_energy = 100
day_events_string = input().split('|')
coins = 100
handled = 0

for events in day_events_string:
    event = events.split('-')

    if event[0] == 'rest':
        energy_gain = int(event[1])

        # gained = min(int(event[1]), 100 - current_energy)
        # current_energy += gained
        # this way we don't have to iterate over the energy gain

        gained = 0
        for gain in range(1, energy_gain+1):
            if current_energy < 100:
                current_energy += 1
                gained += 1

        print(f'You gained {gained} energy.')
        print(f'Current energy: {current_energy}.')

    elif event[0] == 'order':
        if current_energy >= 30:
            coins += int(event[1])
            current_energy -= 30

            print(f'You earned {int(event[1])} coins.')
        else:
            current_energy += 50
            print(f'You had to rest!')

    else:
        if coins >= int(event[1]):
            coins -= int(event[1])
            print(f'You bought {event[0]}.')

        else:
            print(f'Closed! Cannot afford {event[0]}.')
            break


else:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {current_energy}')
