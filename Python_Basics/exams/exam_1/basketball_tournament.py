wins = 0
losses = 0
total_matches = 0

while True:
    command = input()

    if command == 'End of tournaments':
        print(f'{wins/total_matches*100:.2f}% matches win')
        print(f'{losses/total_matches*100:.2f}% matches lost')
        break
    else:
        name_tournament = command

    matches = int(input())

    for match in range(1, matches+1):

        score_home = int(input())
        score_guest = int(input())
        total_matches += 1

        if score_home > score_guest:
            wins += 1
            print(f'Game {match} of tournament {name_tournament}: win with {score_home - score_guest} points.')
        else:
            losses += 1
            print(f'Game {match} of tournament {name_tournament}: lost with {score_guest - score_home} points.')