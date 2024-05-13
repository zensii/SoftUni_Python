sold_games = int(input())
games = {'Hearthstone': 0, 'Fornite': 0, 'Overwatch': 0, 'Others': 0}

for _ in range(sold_games):
    name = input()
    if name not in games:
        games['Others'] += 1
    else:
        games[name] += 1

for game in games:
    print(f'{game} - {games[game]/sold_games*100:.2f}%')

