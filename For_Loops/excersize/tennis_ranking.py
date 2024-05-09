import math

tournaments = int(input())
initial_points = int(input())
wins = 0
points = 0

for _ in range(tournaments):
    position = input()
    if position == 'W':
        points += 2000
        wins += 1
    elif position == 'F':
        points += 1200
    elif position == 'SF':
        points += 720

print(f'Final points: {initial_points + points}')
print(f'Average points: {math.floor(points / tournaments)}')
print(f'{wins/tournaments*100:.2f}%')
