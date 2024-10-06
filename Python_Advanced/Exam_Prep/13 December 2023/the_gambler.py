n = int(input())
matrix = []
money = 100
gambler_pos = []
for row in range(n):
    row_data = list(input())
    for col in range(len(row_data)):
        if row_data[col] == 'G':
            gambler_pos = [row, col]
    matrix.append(row_data)

directions = {'up':(-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
jackpot = False

while True:
    direction = input()
    if direction == 'end':
        break
    next_pos = list(map(sum, zip(gambler_pos, directions[direction])))

    row, col = next_pos

    if 0 <= row < n and 0 <= col < n:

        matrix[gambler_pos[0]][gambler_pos[1]] = '-'
        gambler_pos = next_pos

        if matrix[row][col] == 'J':
            jackpot = True
            money += 100000
            break
        elif matrix[row][col] == 'W':
            money += 100
        elif (
                matrix[row][col] == 'P'):
            money -= 200
            if money <= 0:
                print("Game over! You lost everything!")
                exit()
    else:
        print("Game over! You lost everything!")
        exit()

matrix[gambler_pos[0]][gambler_pos[1]] = 'G'

if jackpot:
    print(f"You win the Jackpot!")
    print(f"End of the game. Total amount: {money}$")
else:
    print(f"End of the game. Total amount: {money}$")

if money > 0:
    [print(*row, sep='') for row in matrix]