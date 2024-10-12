def check_boundary(next_position):
    next_row, next_col  = next_position
    if 0 <= next_row < n and 0 <= next_col < n:
        return True
    return False

n = int(input())
health = 100
matrix = []
directions = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
player_position = []

for row in range(n):
    row_data = list(input())
    for col in range(len(row_data)):
        if row_data[col] == 'P':
            player_position = (row, col)
        elif row_data[col] == 'X':
            exit_position = (row, col)

    matrix.append(row_data)


while health > 0:
    direction = input()

    next_pos = list(map(sum, zip(player_position,directions[direction])))
    if check_boundary(next_pos):
        row, col = next_pos
        matrix[player_position[0]][player_position[1]] = '-'
        player_position = next_pos

        if matrix[row][col] == 'X':
            break

        elif matrix[row][col] == 'M':
            health -= 40
            if health <= 0:
                health = 0
                break
            else:
                matrix[row][col] = '-'

        elif matrix[row][col] == 'H':
            health = min(100, health+15)
            matrix[player_position[0]][player_position[1]] = '-'


matrix[player_position[0]][player_position[1]] = 'P'

if health > 0:
    print("Player escaped the maze. Danger passed!")
else:
    print('Player is dead. Maze over!')

print(f"Player's health: {health} units")
[print(*row, sep='') for row in matrix]
