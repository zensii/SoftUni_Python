def count_attacks(current_row: int, current_col: int) -> int:

    attacks = 0

    for coordinates in knight_moves:
        possible_row_index = current_row + coordinates[0]
        possible_col_index = current_col + coordinates[1]

        if 0 <= possible_row_index < board_size and 0 <= possible_col_index < board_size:
            if matrix[possible_row_index][possible_col_index] == 'K':
                attacks += 1
    return attacks


# Input data
board_size = int(input())
matrix = [list(input()) for _ in range(board_size)]
r, c = 0, 0  # initial coordinates
knight_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
# main logic
removed = 0

while True:
    max_targets = 0
    cur_to_remove_coord = None

    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):

            if matrix[r_index][c_index] == 'K':

                current_knight_targets = count_attacks(r_index, c_index)
                if current_knight_targets > max_targets:
                    max_targets = current_knight_targets
                    cur_to_remove_coord = (r_index, c_index)

    if cur_to_remove_coord is not None:  # terminates if no knight is found that can attack another
        matrix[cur_to_remove_coord[0]][cur_to_remove_coord[1]] = '0'
        removed += 1
    else:
        print(removed)
        break


