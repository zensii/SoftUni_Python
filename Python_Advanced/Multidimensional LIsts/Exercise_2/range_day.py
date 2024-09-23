def shoot(direction):
    bullet_position = shooter_position[:]

    while True:

        next_bullet_position = list(map(sum, zip(bullet_position, moves[direction])))

        if not 0 <= next_bullet_position[0] < field_size or not 0 <= next_bullet_position[1] < field_size:
            break

        else:
            if next_bullet_position in targets:
                targets_hit.append(next_bullet_position)
                targets.remove(next_bullet_position)
                matrix[next_bullet_position[0]][next_bullet_position[1]] = '.'
                break

        bullet_position = next_bullet_position


def move_0(direction, steps) -> None:
    """
    same as the move function below
    :param direction:
    :param steps:
    :return:
    """
    global shooter_position
    new_shooter_position = shooter_position

    for step in range(steps):
        new_shooter_position = list(map(sum, zip(new_shooter_position, moves[direction])))

    if not 0 <= new_shooter_position[0] < field_size or not 0 <= new_shooter_position[
        1] < field_size or new_shooter_position in targets:
        return

    else:
        matrix[shooter_position[0]][shooter_position[1]] = '.'
        shooter_position = new_shooter_position
        matrix[new_shooter_position[0]][new_shooter_position[1]] = 'A'


def move(direction, steps) -> None:
    """
    this function calculates if the index of the required move action is valid and if so updates the matrix. Another
    implementation of move_0 function
    :param direction:
    :param steps:
    :return:
    """
    global shooter_position

    row = shooter_position[0] + steps * moves[direction][0]
    col = shooter_position[1] + steps * moves[direction][1]

    if 0 <= row < field_size and 0 <= col < field_size and matrix[row][col] == '.':

        matrix[shooter_position[0]][shooter_position[1]] = '.'
        shooter_position = [row, col]
        matrix[shooter_position[0]][shooter_position[1]] = 'A'


field_size = 5

matrix = [input().split() for _ in range(field_size)]
moves = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}

n = int(input())

shooter_position = None
targets = []
targets_hit = []

for index_r, row in enumerate(matrix):
    for index_c, col in enumerate(row):

        if matrix[index_r][index_c] == 'A':
            shooter_position = [index_r, index_c]
        elif matrix[index_r][index_c] == 'x':
            target = [index_r, index_c]
            targets.append(target)



for _ in range(n):

    command = input().split()

    if command[0] == 'move':
        direction, steps = command[1], command[2]

        move(direction, int(steps))

    elif command[0] == 'shoot':
        direction = command[1]
        shoot(direction)

    if not targets:
        print(f"Training completed! All {len(targets_hit)} targets hit.")
        break

if targets:
    print(f"Training not completed! {len(targets)} targets left.")

print(*targets_hit, sep='\n')


