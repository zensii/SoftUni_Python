from copy import deepcopy

rows, cols = list(map(int, input().split()))
n = 3
matrix = [list(map(int, input().split())) for row in range(rows)]
max_sum = float('-inf')
max_matrix = None

for row_index in range(rows-(n-1)):
    for col_index in range(cols-(n-1)):

        temp_matrix = []
        temp_sum = 0
        for i in range(n):
            temp_row = []
            for j in range(n):
                temp_row.append(matrix[row_index+i][col_index+j])

            temp_sum += sum(temp_row)
            temp_matrix.append(temp_row)

        if temp_sum >= max_sum:
            max_sum = temp_sum
            max_matrix = deepcopy(temp_matrix)

print(f"Sum = {max_sum}")
print(*[' '.join(map(str, row)) for row in max_matrix], sep='\n')
