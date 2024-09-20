rows, cols = list(map(int, input().split()))

first_char_ascii = ord('a')
matrix = []

for row_index in range(rows):
    temp_row = []
    temp_ascii = first_char_ascii + row_index

    for col_index in range(cols):
        temp_col = ''.join(map(chr, [temp_ascii, temp_ascii+col_index, temp_ascii]))
        temp_row.append(temp_col)

    matrix.append(temp_row)

for row in matrix:
    print(' '.join(row))

