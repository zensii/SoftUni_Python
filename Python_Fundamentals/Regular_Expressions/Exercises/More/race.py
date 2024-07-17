import re
players = {}
participants = input()
characters = input()

while characters != 'end of race':
    distance = 0
    name = ''.join(re.findall(r'[a-zA-Z]+', characters))
    if name in participants:
        distance = sum(int(num) for num in re.findall(r'\d', characters))
        if name not in players:
            players[name] = distance
        else:
            players[name] += distance

    characters = input()

leaderboard = sorted(players.items(), key=lambda x: x[1], reverse=True)


print(f'1st place: {leaderboard[0][0]}')
print(f'2nd place: {leaderboard[1][0]}')
print(f'3rd place: {leaderboard[2][0]}')
