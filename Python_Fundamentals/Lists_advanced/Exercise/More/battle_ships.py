def battleships():

    destroyed_ships = 0

    for attack in attacks:
        coordinates = attack.split('-')
        row = int(coordinates[0])
        column = int(coordinates[1])
        attacked_ship = battlefield[row][column]

        if attacked_ship > 0:
            attacked_ship -= 1
            battlefield[row][column] = attacked_ship

            if attacked_ship == 0:
                destroyed_ships += 1

    return destroyed_ships


rows = int(input())
battlefield = [list(map(int, input().split())) for _ in range(rows)]
attacks = (input().split())

print(battleships())