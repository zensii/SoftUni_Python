def get_bunny_position(r: int, r_data: list) -> tuple[int, int]:

    bunny_start_position = (r, r_data.index('B'))
    return bunny_start_position


def get_trap_positions(r: int, r_data: list) -> list[tuple[int, int]]:
    cur_trap_positions = []
    for col_index, position in enumerate(r_data):
        if position == 'X':
            cur_trap_positions.append((r, col_index))
    return cur_trap_positions


def get_directions() -> dict[str, list[tuple[int, int]]]:

    directions_dict = {'up':[], 'down':[], 'left':[], 'right':[]}

    for row_index, row_data in enumerate(matrix):
        for col_index, col_value in enumerate(row_data):

            coordinate = (row_index, col_index)

            if row_index == bunny_position[0] and 0 <= col_index < bunny_position[1]:
                directions_dict['left'].append(coordinate)

            elif row_index == bunny_position[0] and bunny_position[1] < col_index < n:
                directions_dict['right'].append(coordinate)

            elif col_index == bunny_position[1] and 0 <= row_index < bunny_position[0]:
                directions_dict['up'].append(coordinate)

            elif col_index == bunny_position[1] and bunny_position[0] < row_index < n:
                directions_dict['down'].append(coordinate)

    directions_dict['up'].reverse()
    directions_dict['left'].reverse()

    return directions_dict


def check_for_traps(directions):

    for key, direction_coords in directions.items():
        for coordinate in direction_coords:
            if coordinate in trap_positions:
                directions[key] = directions[key][:directions[key].index(coordinate)]
                break


def calculate_eggs(directions) -> tuple[int, str]:
    max_eggs = 0
    best_path = None

    for key, direction_coords in directions.items():
        eggs = 0
        for coordinate in direction_coords:
            eggs += matrix[coordinate[0]][coordinate[1]]
            if  best_path is None or max_eggs < eggs:
                max_eggs = eggs
                best_path = key

    return max_eggs, best_path


# input data
n = int(input())
matrix = []
trap_positions = []
bunny_position = None

for row in range(n):
    row_data = list(map(lambda x: int(x) if x.isdigit() or x.startswith('-') else x, input().split()))
    matrix.append(row_data)
    if 'B' in row_data:
        bunny_position = get_bunny_position(row, row_data)
    if 'X' in row_data:
        trap_positions.extend(get_trap_positions(row, row_data))

directions = get_directions()
check_for_traps(directions)
collected_eggs, best_path = calculate_eggs(directions)

print(best_path)

for direction in directions[best_path]:
    print(f"[{direction[0]}, {direction[1]}]")

print(collected_eggs)
