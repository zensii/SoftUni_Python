

def explode(row, col):
    value = matrix[row][col]
    for i in range(-1, 2): # size of bomb blast
        for j in range(-1, 2):
            try:
                if matrix[row+i][col+j] > 0 and row+i >= 0 and col+j >= 0:
                    matrix[row+i][col+j] -= value
            except IndexError:
                continue


rows = int(input())
matrix = [list(map(int, input().split())) for row in range(rows)]
coordinates = [tuple(int(el) for el in coord.split(',')) for coord in input().split()]


for coord in coordinates:
    if matrix[coord[0]][coord[1]] > 0:
        explode(coord[0], coord[1])
alive_cells = 0
alive_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_sum += el
print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_sum}')
for row in matrix:
    print(' '.join(str(el) for el in row))
