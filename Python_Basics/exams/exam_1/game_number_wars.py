player_one = input()
player_two = input()
player_one_points = 0
player_two_points = 0

while True:

    command = input()
    if command == "End of game":
        print(f'{player_one} has {player_one_points} points')
        print(f'{player_two} has {player_two_points} points')
        break
    else:
        card_one = int(command)
    card_two = int(input())

    if card_one > card_two:
        player_one_points += card_one - card_two
    elif card_one < card_two:
        player_two_points += card_two - card_one
    else:
        one_extra = int(input())
        two_extra = int(input())
        print('Number wars!')
        if one_extra > two_extra:
            print(f'{player_one} is winner with {player_one_points} points')
        else:
            print(f'{player_two} is winner with {player_two_points} points')
        break
