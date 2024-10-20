def check_valid_move(next_position: list[int]) -> bool:
    next_row, next_col = next_position
    if 0 <= next_row < n and 0 <= next_row < m:
        return True
    return False


n, m = list(map(int, input().split(', ')))
bomb_location = None
ct_location = None
ct_dead = False
bomb_defused = False
field = []
TIME = 16
directions = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}

for row in range(n):
    row_data = list(input())
    if 'B' in row_data:
        bomb_location = [row, row_data.index('B')]
    elif 'C' in row_data:
        ct_location = [row, row_data.index('C')]
    field.append(row_data)

while TIME > 0:

    command = input()
    TIME -= 1

    if command == 'defuse':
        if field[ct_location[0]][ct_location[1]] == 'B':
            if TIME >= 4:
                field[ct_location[0]][ct_location[1]] = 'D'
                bomb_defused = True
                break
            else:
                field[ct_location[0]][ct_location[1]] = 'X'
                ct_dead = True
                break
        else:
            TIME -= 2
    else:
        direction = command
        next_pos = list(map(sum, zip(ct_location, directions[direction])))
        if check_valid_move(next_pos):
            row, col = next_pos
            if field[row][col] == 'T':
                field[row][col] = '*'
                ct_dead = True
                break
            elif field[row][col] == 'B':
                continue

            ct_location = next_pos

#TODO



