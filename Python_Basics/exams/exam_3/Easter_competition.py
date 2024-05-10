cakes = int(input())
max_score = 0
winner = ''

for cake in range(cakes):

    name = input()
    total_score = 0

    if winner == '':
        winner = name

    while True:
        user_input = input()

        if user_input == 'Stop':
            print(f'{name} has {total_score} points.')
            if name == winner:
                print(f'{winner} is the new number 1!')
            break

        user_score = int(user_input)
        total_score += user_score

        if total_score > max_score:
            max_score = total_score
            winner = name
print(f'{winner} won competition with {max_score} points!')
