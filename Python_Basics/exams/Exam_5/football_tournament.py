team_name = input()
games_played = int(input())
W = 0
D = 0
L = 0
points = 0

for game in range(games_played):
    result = input()
    if result == 'W':
        W += 1
        points += 3
    elif result == 'D':
        D += 1
        points += 1
    elif result == 'L':
        L += 1

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f'{team_name} has won {points} points during this season.')
    print('Total stats:')
    print(f'## W: {W}')
    print(f'## D: {D}')
    print(f'## L: {L}')
    print(f'Win rate: {W / games_played * 100:.2f}%')
