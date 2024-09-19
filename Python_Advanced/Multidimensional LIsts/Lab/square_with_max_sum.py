from copy import deepcopy

rows, cols = map(int, input().split(', '))
matrix = [list(map(int, input().split(', '))) for row in range(rows)]

n = 2 # sub matrix size. Can be made to be input()
max_sum = 0
max_matrix = None
# initialising the sub matrix
sub_matrix = [[0 for _ in range(n)] for _ in range(n)]

# traversing the main matrix up to length minus the len(sub_matrix). -1 is because ranges start from 0
for row in range(rows - (n-1)):
    for col in range(cols - (n-1)):

        # initialising the current sum and updating the sub_matrix as per the new zero point
        current_sum = 0
        for i in range(n):
            for j in range(n):
                sub_matrix[i][j] = matrix[row+i][col+j]
                current_sum += sub_matrix[i][j]

                # updating max variables if needed
        if current_sum > max_sum:
            max_matrix = deepcopy(sub_matrix)
            max_sum = current_sum


for row in max_matrix:
    print(*row, sep=' ')
print(max_sum)
