def gain_star(stars):
    stars += 1
    return stars


def lose_star(stars):
    stars -= 1
    return stars


def next_pos(direction, cur_position):
    # cur_position[0] += directions[direction][0]
    # cur_position[1] += directions[direction][1]
    pos = tuple(x+y for x, y in zip(cur_position, directions[direction]))
    return pos


n = int(input())
field = []
player_pos = None
stars = 2
directions = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}

for row in range(n):
    row_data = input().split()
    field.append(row_data)
    for col in range(len(row_data)):
        if row_data[col] == 'P':
            player_pos = (row, col)

while 0 < stars < 10:

    direction = input()
    next_player_pos = next_pos(direction, player_pos)
    if 0 <= next_player_pos[0] < n and 0 <= next_player_pos[1] < n:

        if field[next_player_pos[0]][next_player_pos[1]] in '*.':

            if field[next_player_pos[0]][next_player_pos[1]] == '*':
                stars = gain_star(stars)

            field[player_pos[0]][player_pos[1]] = '.'
            field[next_player_pos[0]][next_player_pos[1]] = 'P'
            player_pos = next_player_pos

        elif field[next_player_pos[0]][next_player_pos[1]] == '#':
            stars = lose_star(stars)
    else:
        field[player_pos[0]][player_pos[1]] = '.'
        player_pos = (0, 0)
        if field[player_pos[0]][player_pos[1]] == '*':
            stars = gain_star(stars)

        field[player_pos[0]][player_pos[1]] = 'P'

if stars == 0:
    print("Game over! You are out of any stars.")
else:
    print("You won! You have collected 10 stars.")

print(f"Your final position is [{player_pos[0]}, {player_pos[1]}]")

[print(*row) for row in field]
