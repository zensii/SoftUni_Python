n = int(input())
armor = 300
matrix = []
directions = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
jet_position = []
enemy_jets = []

for row in range(n):
    row_data = list(input())
    for col in range(len(row_data)):
        if row_data[col] == 'J':
            jet_position = (row, col)
        elif row_data[col] == 'E':
            enemy_jets.append((row, col))

    matrix.append(row_data)

while armor > 0 and enemy_jets:
    direction = input()

    next_pos = list(map(sum, zip(jet_position, directions[direction])))

    row, col = next_pos

    matrix[jet_position[0]][jet_position[1]] = '-'
    jet_position = next_pos

    if matrix[row][col] == 'E':
        enemy_jets.pop()
        if enemy_jets:
            armor -= 100
            if armor <= 0:
                armor = 0
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
                break
        else:
            print("Mission accomplished, you neutralized the aerial threat!")

        matrix[row][col] = '-'

    elif matrix[row][col] == 'R':
        armor = 300
        matrix[row][col] = '-'

matrix[jet_position[0]][jet_position[1]] = 'J'

[print(*row, sep='') for row in matrix]