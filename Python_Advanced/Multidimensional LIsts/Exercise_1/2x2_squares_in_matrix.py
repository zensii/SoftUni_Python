rows, cols = list(map(int, input().split()))

matrix = [list(input().split()) for row in range(rows)]
tot_sum = 0

for row_index in range(rows-1):
    temp_matrix = []

    for col_index in range(cols-1):
        top_left = matrix[row_index][col_index]
        top_right = matrix[row_index][col_index+1]
        bot_left = matrix[row_index+1][col_index]
        bot_right = matrix[row_index+1][col_index+1]

        if top_left == top_right == bot_left == bot_right:
            tot_sum += 1


print(tot_sum)
