def check_valid_move(next_position: list[int], n, m) -> bool:
    next_row, next_col = next_position
    if 0 <= next_row < n and 0 <= next_col < m:
        return True
    return False


n, m = list(map(int, input().split(', ')))
bomb_location = None
ct_location = None
bomb_exploded = False
time_for_success = 0
field = []
TIME = 16
directions = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}

for row in range(n):
    row_data = list(input())
    if 'B' in row_data:
        bomb_location = [row, row_data.index('B')]
    if 'C' in row_data:
        ct_location = [row, row_data.index('C')]
    field.append(row_data)


while TIME > 0:

    command = input()

    if command == 'defuse':
        if field[ct_location[0]][ct_location[1]] == 'B':
            if TIME >= 4:
                field[ct_location[0]][ct_location[1]] = 'D'
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {TIME - 4} second/s remaining.")
                break

            else:
                field[ct_location[0]][ct_location[1]] = 'X'
                time_for_success = 4 - TIME
                bomb_exploded = True
                break
        else:
            TIME -= 2
            if TIME <= 0:
                break
    else:
        TIME -= 1
        direction = command
        next_pos = list(map(sum, zip(ct_location, directions[direction])))
        if check_valid_move(next_pos, n, m):
            row, col = next_pos
            if field[row][col] == 'T':
                field[row][col] = '*'
                print("Terrorists win!")
                break

            ct_location = next_pos


if bomb_exploded or TIME <= 0:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {time_for_success} second/s.")

[print(''.join(row)) for row in field]