rows = int(input())
matrix = []
sum_primary = 0
sum_secondary = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split()])

#sum primary diagonal
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if row_index == col_index:
            sum_primary += matrix[row_index][col_index]
# sum secondary diagonal
#         if row_index + col_index == rows-1:
#             sum_secondary += matrix[row_index][col_index]

print(sum_primary)
# print(sum_secondary)
