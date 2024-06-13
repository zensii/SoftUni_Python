def distribute_loot(loot):
    items_found = loot.split()

    for i in range(0, len(items_found), 2):
        component = items_found[i + 1].lower()
        value = int(items_found[i])
        if component in legendary_components_inventory.keys():
            legendary_components_inventory[component] += value
            if legendary_components_inventory[component] >= 250:
                break
        else:
            if component in junk.keys():
                junk[component] += value
            else:
                junk[component] = value


def check_legendary(legendary_components_inventory):

    legendary_items = {'shards': 'Shadowmourne',
                       'fragments': 'Valanyr',
                       'motes': 'Dragonwrath'
                       }

    for component in legendary_components_inventory.keys():
        if legendary_components_inventory[component] >= 250:
            print(f'{legendary_items[component]} obtained!')
            legendary_components_inventory[component] -= 250
            return True
    return False


junk = {}
legendary_components_inventory = {'shards': 0, 'fragments': 0, 'motes': 0}

while True:
    found_loot = input()
    distribute_loot(found_loot)
    if check_legendary(legendary_components_inventory):
        break

for item, value in legendary_components_inventory.items():
    print(f'{item}: {value}')

for item, value in junk.items():
    print(f'{item}: {value}')
