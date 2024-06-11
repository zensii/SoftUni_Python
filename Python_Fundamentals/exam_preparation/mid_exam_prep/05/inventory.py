def collect(inventory, item):
    if item not in inventory:
        inventory.append(item)


def drop(inventory, item):
    if item in inventory:
        inventory.remove(item)


def combine(inventory, items):
    old_item = items.split(':')[0]
    new_item = items.split(':')[1]
    if old_item in inventory:
        inventory.insert(inventory.index(old_item)+1, new_item)


def renew(inventory, item):
    if item in inventory:
        inventory.remove(item)
        inventory.append(item)


def craft(inventory):
    return ', '.join(inventory)


def commands(journal):
    command = input().split(' - ')
    end = False

    if command[0] == 'Craft!':
        end = True
        return end, None, None
    else:
        action = command[0]
        item = command[1]
        return end, action, item


def main():

    journal = input().split(', ')

    while True:
        end, action, item = commands(journal)
        if end:
            print(craft(journal))
            break

        if action == 'Collect':
            collect(journal, item)
        if action == 'Drop':
            drop(journal, item)
        if action == 'Combine Items':
            combine(journal, item)
        if action == 'Renew':
            renew(journal, item)


if __name__ == '__main__':
    main()
