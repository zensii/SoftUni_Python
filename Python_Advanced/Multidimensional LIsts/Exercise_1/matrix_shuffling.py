rows, cols = list(map(int, input().split()))
matrix = [input().split() for row in range(rows)]
commands = []

while True:
    command = input()
    if command == 'END':
        break

    commands.append(command)

for command in commands:

    line = command.split()

    if len(line) == 5 and line[0] == 'swap':
        row1, col1, row2, col2 = map(int, line[1:])
        try:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print(*[' '.join(map(str, row)) for row in matrix], sep='\n')
        except IndexError:
            print('Invalid input!')

    else:
        print('Invalid input!')
        continue
