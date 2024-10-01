def next_position(move_direction, cur_position):
    next_pos = tuple((x+y) % n for x, y in zip(cur_position, directions[move_direction]))
    return next_pos


n = int(input())
matrix = []
INITIAL_BEE_ENERGY = 15
bee_energy = INITIAL_BEE_ENERGY
bee_position = None
hive_pos = None
nectar_collected = 0
drink_nectar = False

directions = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}


for row in range(n):
    row_data = list(map(lambda x: int(x) if x.isdigit() else x, list(input())))
    matrix.append(row_data)
    for col in range(n):
        if matrix[row][col] == 'B':
            bee_position = (row, col)
        elif matrix[row][col] == 'H':
            hive_pos = (row, col)

while bee_energy > 0 and bee_position != hive_pos:
    direction = input()
    bessy_next_pos = next_position(direction, bee_position)

    r, c = bessy_next_pos[0],  bessy_next_pos[1]

    if type(matrix[r][c]) == int:
        nectar_collected += matrix[r][c]

    bee_energy -= 1

    if bee_energy == 0 and nectar_collected > 30 and drink_nectar is False:
        bee_energy += nectar_collected - 30
        nectar_collected = 30
        drink_nectar = True

    matrix[bee_position[0]][bee_position[1]] = '-'
    bee_position = bessy_next_pos
    matrix[bee_position[0]][bee_position[1]] = 'B'


if nectar_collected >= 30 and bee_position == hive_pos:
    print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")

elif bee_position == hive_pos:
    print("Beesy did not manage to collect enough nectar.")

else:
    print("This is the end! Beesy ran out of energy.")

print(*[''.join(list(map(str, row))) for row in matrix], sep='\n')
