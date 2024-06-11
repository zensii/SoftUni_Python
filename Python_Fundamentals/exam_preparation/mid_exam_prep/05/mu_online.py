def potion(health, potion):
    new_health = health + potion
    if new_health > 100:
        new_health = 100
        amount = new_health - health
    else:
        amount = potion
    print(f'You healed for {amount} hp.')
    print(f'Current health: {new_health} hp.')
    return new_health


def chest(current_bitcoins, chest):
    current_bitcoins += chest
    print(f'You found {chest} bitcoins.')
    return current_bitcoins


def encounter(current_health, monster, damage):
    dead = False
    current_health -= damage
    if current_health > 0:
        print(f'You slayed {monster}.')
    else:
        dead = True
    return current_health, dead


def main():
    health = 100
    bitcoins = 0
    dungeon = input().split('|')
    room_count = 0

    for room in dungeon:
        room_action = room.split()
        room_count += 1

        if room_action[0] == 'potion':
            health = potion(health, int(room_action[1]))
        elif room_action[0] == 'chest':
            bitcoins = chest(bitcoins, int(room_action[1]))
        else:
            health, dead = encounter(health, room_action[0], int(room_action[1]))

            if dead:
                print(f'You died! Killed by {room_action[0]}.')
                print(f'Best room: {room_count}')
                break
    else:
        print(f'You\'ve made it!')
        print(f'Bitcoins: {bitcoins}')
        print(f'Health: {health}')


if __name__ == '__main__':
    main()