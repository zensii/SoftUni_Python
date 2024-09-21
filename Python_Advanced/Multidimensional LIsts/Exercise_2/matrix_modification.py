n = int(input())
matrix = [list(map(int, input().split())) for _ in range(int(n))]

while True:
    prompt = input()
    if prompt == 'END':
        break

    command, row, col, value = list(map(lambda x: int(x) if x.isdigit() or x.startswith('-') else x, prompt.split()))

    if 0 <= row < n and 0 <= col < len(matrix[0]):
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for row in matrix:
    print(*row)

