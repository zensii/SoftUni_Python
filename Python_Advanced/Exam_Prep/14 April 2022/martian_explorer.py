N = 6
matrix = []
rover_position = None
water_found = False
concrete_found = False
metal_found = False
directions = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}

for row in range(N):
    col_data = input().split(' ')
    matrix.append(col_data)
    if not rover_position and 'E' in col_data:
        rover_position = [row, col_data.index('E')]

movements = input().split(', ')

for movement in movements:
    next_row = (rover_position[0] + directions[movement][0]) % N
    next_col = (rover_position[1] + directions[movement][1]) % N

    if matrix[next_row][next_col] == 'W':
        water_found = True
        print(f"Water deposit found at ({next_row}, {next_col})")
    elif matrix[next_row][next_col] == 'M':
        metal_found = True
        print(f"Metal deposit found at ({next_row}, {next_col})")
    elif matrix[next_row][next_col] == 'C':
        concrete_found = True
        print(f"Concrete deposit found at ({next_row}, {next_col})")
    elif matrix[next_row][next_col] == 'R':
        print(f"Rover got broken at ({next_row}, {next_col})")
        break
    rover_position = [next_row, next_col]

if water_found and concrete_found and metal_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")