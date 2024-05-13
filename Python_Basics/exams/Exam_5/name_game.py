winner = None
max_score = 0

while True:
    score = 0
    user_input = input()
    if user_input == 'Stop':
        break

    name = user_input
    for letter in name:

        number = int(input())
        if number == ord(letter):
            score += 10
        else:
            score += 2

    if score >= max_score:
        max_score = score
        winner = name
print(f'The winner is {winner} with {max_score} points!')
