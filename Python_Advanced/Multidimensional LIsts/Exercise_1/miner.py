def find_start_pos() -> list[int] | None:

    position = None
    for index_row, row in enumerate(matrix):
        for index_col, col in enumerate(row):
            if matrix[index_row][index_col] == 's':
                position = [index_row, index_col]

    return position


def find_max_coal() -> int:
    coal = 0

    for index_row, row in enumerate(matrix):
        for index_col, col in enumerate(row):

            if matrix[index_row][index_col] == 'c':
                coal += 1

    return coal


def move():
    global current_pos

    if command == 'up' and current_pos[0] != 0:
        current_pos[0] -= 1
    elif command == 'down' and current_pos[0] != n-1:
        current_pos[0] += 1
    elif command == 'left' and current_pos[1] != 0:
        current_pos[1] -= 1
    elif command == 'right' and current_pos[1] != n - 1:
        current_pos[1] += 1



def check_location(index_row, index_col):
    """
    This function checks the current location for loot or if the exit is found.
    if loot is found it updates the global collected variable. Then checks if all possible loot is found
    and triggers end of the program
    if the end location is found it triggers the end of the program

    :param index_row:
    :param index_col:
    :return:
    """
    global found_coal

    if matrix[index_row][index_col] == 'c':
        found_coal += 1
        matrix[index_row][index_col] = '*'

        if found_coal == max_coal:
            return True # all possible coal has been collected

    elif matrix[index_row][index_col] == 'e':
        return True # found the end location
    return False


n = int(input())
commands = input().split()
matrix = [input().split() for _ in range(n)]


current_pos = find_start_pos()
max_coal = find_max_coal()
found_coal = 0
found_exit = False

for command in commands:
    if current_pos is not None:
        move()
        # check what is in the current location and collects coal or finds exit
        if check_location(current_pos[0], current_pos[1]):
            break

if found_coal == max_coal:
    print(f"You collected all coal! ({current_pos[0]}, {current_pos[1]})")

elif matrix[current_pos[0]][current_pos[1]] == 'e':
    print(f"Game over! ({current_pos[0]}, {current_pos[1]})")
else:
    print(f"{max_coal - found_coal} pieces of coal left. ({current_pos[0]}, {current_pos[1]})")
