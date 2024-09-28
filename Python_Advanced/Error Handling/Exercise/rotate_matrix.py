class MatrixContentError(Exception):
    """The matrix must consist of only integers"""
    pass

class MatrixSizeError(Exception):
    """The size of the matrix is not a perfect square"""
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


mtrx = []

while True:

    line = input().split()
    if not all(char.isdigit() for char in line):
        raise MatrixContentError(MatrixContentError.__doc__)

    if not line:
        break
    mtrx.append(line)


if any(len(line) != len(mtrx) for line in mtrx):
    raise MatrixSizeError(MatrixSizeError.__doc__)

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')