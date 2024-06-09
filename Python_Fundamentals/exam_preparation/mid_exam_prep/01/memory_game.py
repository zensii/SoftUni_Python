def punish_cheat(string, current_move):

    element_to_add = f'-{current_move}a'
    string.insert(len(string) // 2, element_to_add)
    string.insert(len(string) // 2, element_to_add)
    print('Invalid input! Adding additional elements to the board')
    return string


def guess(string):
    player_guess = player_input.split(' ')
    first_index = int(player_guess[0])
    second_index = int(player_guess[1])

    if first_index == second_index or not (0 <= first_index < len(string)) or not (0 <= second_index < len(string)):
        punish_cheat(string, moves)

    elif string[first_index] == string[second_index]:
        print(f'Congrats! You have found matching elements - {string[first_index]}!')
        string.pop(max(first_index, second_index))
        string.pop(min(first_index, second_index))
    else:
        print('Try again!')

    return string


sequence = [element for element in input().split(' ')]
moves = 0
while len(sequence) != 0:
    player_input = input()
    if player_input == 'end':
        print(f'Sorry you lose :(')
        print(' '.join(map(str, sequence)))
        break
    else:
        moves += 1
        guess(sequence)

else:
    print(f"You have won in {moves} turns!")
