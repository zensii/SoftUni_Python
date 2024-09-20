from collections import deque

rows, cols = list(map(int, input().split()))
string = deque(input())
matrix = []

for row_index in range(rows):
    temp_row = deque()
    for col_index in range(cols):
        if row_index % 2 == 0:
            temp_row.append(string[0])
        else:
            temp_row.appendleft(string[0])

        string.rotate(-1)

    matrix.append(temp_row)

for row in matrix:
    print(''.join(row))