n = int(input())

matrix = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(n)]
commands = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
tee_bags = 0
alice_position = None
rabbit_hole = None

for index_r, row in enumerate(matrix):
    for index_c, col in enumerate(row):

        if matrix[index_r][index_c] == 'A':
            alice_position = [index_r, index_c]
            matrix[index_r][index_c] = '*'
        elif matrix[index_r][index_c] == 'R':
            rabbit_hole = [index_r, index_c]

while tee_bags < 10:

    move_command = input()
    alice_new_position = [sum(i) for i in zip(alice_position, commands[move_command])]
    alice_position = alice_new_position

    if not 0 <= alice_position[0] < n or not 0 <= alice_position[1] < n:
        break

    else:
        if matrix[alice_position[0]][alice_position[1]] == 'R':
            matrix[alice_position[0]][alice_position[1]] = '*'
            break

        else:
            try:
                tee_bags += matrix[alice_position[0]][alice_position[1]]

            except TypeError:
                pass

            matrix[alice_position[0]][alice_position[1]] = '*'

if tee_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]