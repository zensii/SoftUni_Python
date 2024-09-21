def find_start_pos() -> list[int]:

    for index_row, row in enumerate(matrix):
        for index_col, col in enumerate(row):
            if matrix[index_row][index_col] == 'P':
                start_position = [index_row, index_col]

                return start_position


def move() -> None:

    if command == 'U':
        current_pos[0] -= 1
    elif command == 'D':
        current_pos[0] += 1
    elif command == 'L':
        current_pos[1] -= 1
    elif command == 'R':
        current_pos[1] += 1


def get_cur_matrix_state() -> list[list]:

    from copy import deepcopy
    return deepcopy(matrix)


def check_win() -> bool:

    if current_pos[0] < 0 or current_pos[1] < 0 or current_pos[0] >= rows or current_pos[1] >= cols:
        return True


def check_lost(field: str) -> bool:

    if field == 'B':
        return True


def bunny_breed() -> None:

    temp_matrix = get_cur_matrix_state()
    for r_index, row in enumerate(temp_matrix):
        for c_index, col in enumerate(row):
            if col == 'B':
                if r_index != rows - 1:
                    matrix[r_index + 1][c_index] = 'B'
                if c_index != cols - 1:
                    matrix[r_index][c_index + 1] = 'B'
                if r_index != 0:
                    matrix[r_index - 1][c_index] = 'B'
                if c_index != 0:
                    matrix[r_index][c_index - 1] = 'B'


def get_field() -> str:

    return matrix[current_pos[0]][current_pos[1]]


def print_matrix() -> None:
    for row in matrix:
        print(''.join(row))


# Input data
rows, cols = list(map(int, input().split()))
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

commands = list(input())


# main logic
win = False
lost = False
current_pos = find_start_pos()

for command in commands:

    last_pos = current_pos.copy()
    matrix[current_pos[0]][current_pos[1]] = '.'
    move()
    bunny_breed()

    if check_win():
        print_matrix()
        print(f"won: {last_pos[0]} {last_pos[1]}")
        break
    else:
        if check_lost(get_field()):
            print_matrix()
            print(f"dead: {current_pos[0]} {current_pos[1]}")
            break
