def move(direction):

    row = santa_location[0] + moves[direction][0]
    col = santa_location[1] + moves[direction][1]
    new_location = [row, col]

    return new_location


def check_valid_move(new_location: list[int]) -> True | False:

    if 0 <= new_location[0] < matrix_size and 0 <= new_location[1] < matrix_size:
        return True
    return False


def check_next_location(next_location):

        return matrix[next_location[0]][next_location[1]]


def drop_presents():
    global presents, good_kids, good_kids_visited
    presents -= 1
    good_kids -= 1
    good_kids_visited += 1


presents = int(input())
matrix_size = int(input())
moves = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
matrix = []
santa_location = []

good_kids = 0
good_kids_visited = 0

for row in range(matrix_size):
    matrix.append(input().split())
    for index, col in enumerate(matrix[row]):

        if col == 'S':
            santa_location = [row, index]
        elif col == 'V':
            good_kids += 1


while presents:
    direction = input()
    if direction == 'Christmas morning':
        break
    next_location = move(direction)

    if check_valid_move(next_location):

        matrix[santa_location[0]][santa_location[1]] = '-'
        santa_location = next_location

        next_stop = check_next_location(next_location)

        if next_stop == 'V':
            drop_presents()

        elif next_stop == 'C':

            for happy_direction in moves.keys():
                happy_row, happy_col = move(happy_direction)

                if matrix[happy_row][happy_col] in 'VX' and presents > 0:
                    presents -= 1
                    if matrix[happy_row][happy_col] == 'V':
                        good_kids -= 1
                        good_kids_visited += 1
                    matrix[happy_row][happy_col] = '-'

        matrix[santa_location[0]][santa_location[1]] = 'S'

        if presents == 0 and good_kids > 0:
            print("Santa ran out of presents!")

[print(*row) for row in matrix]
if good_kids > 0:
    print(f"No presents for {good_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {good_kids_visited} happy nice kid/s.")
