def loot(chests, loot):
    loot.pop(0)
    for item in loot:
        if item not in chests:
            chests.insert(0, item)


def drop(chests, number):
    index = int(number[1])
    if 0 <= index < len(chests):
        chests.append(chests.pop(index))


def steal(chests, count):
    stolen_items = []
    amount_stolen = int(count[1])
    if amount_stolen >= len(chests):
        stolen_items = chests.copy()
        chests.clear()
    else:
        for item in range(amount_stolen):
            stolen_items.insert(0, (chests.pop(-1)))
    print(', '.join(stolen_items))


def main():
    chest_loot = input().split('|')
    command = input()

    while command != 'Yohoho!':

        command = command.split()
        action = command[0]
        if action == 'Loot':
            loot(chest_loot, command)
        if action == 'Drop':
            drop(chest_loot, command)
        if action == 'Steal':
            steal(chest_loot, command)

        command = input()

    if len(chest_loot) == 0:
        print("Failed treasure hunt.")
    else:
        average_gain = sum(len(item) for item in chest_loot) / len(chest_loot)
        print(f'Average treasure gain: {average_gain:.2f} pirate credits.')


if __name__ == '__main__':
    main()
