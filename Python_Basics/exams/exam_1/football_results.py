first_game = input()
second_game = input()
third_game = input()
home_wins = 0
home_loses = 0
draws = 0

if first_game[0] > first_game[2]:
    home_wins += 1
elif first_game[0] < first_game[2]:
    home_loses += 1
else:
    draws += 1
if second_game[0] > second_game[2]:
    home_wins += 1
elif second_game[0] < second_game[2]:
    home_loses += 1
else:
    draws += 1
if third_game[0] > third_game[2]:
    home_wins += 1
elif third_game[0] < third_game[2]:
    home_loses += 1
else:
    draws += 1
print(f'Team won {home_wins} games.')
print(f'Team lost {home_loses} games.')
print(f'Drawn games: {draws}')
