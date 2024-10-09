def check_next_move(next_player_position: tuple) -> bool:
    if 0 <= next_player_position[0] < n and 0 <= next_player_position[1] < m and next_player_position not in obstacles:
        return True
    return False


def next_position(next_direction: str) -> tuple:
    return tuple(map(sum, zip(player_pos, directions[next_direction])))


n, m = map(int, input().split(' '))
player_pos = None
matrix = []
directions = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
obstacles = []
touches = 0
moves = 0

for row in range(n):
    col_data = input().split(' ')
    matrix.append(col_data)
    if 'B' in col_data:
        player_pos = row, col_data.index('B')
    for col in range(m):
        if col_data[col] == 'O':
            obstacles.append((row, col))

while True:
    direction = input()
    if direction == 'Finish':
        break

    next_pos = next_position(direction)

    if check_next_move(next_pos):
        matrix[player_pos[0]][player_pos[1]] = '-'
        player_pos = next_pos
        moves += 1

        if matrix[player_pos[0]][player_pos[1]] == 'P':
            touches += 1
            matrix[player_pos[0]][player_pos[1]] = 'B'

            if touches == 3:
                break

print('Game over!')
print(f"Touched opponents: {touches} Moves made: {moves}")

