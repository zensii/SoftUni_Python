time_line = [int(seconds) for seconds in input().split()]
time_left = 0
time_right = 0

mid = len(time_line) // 2

# time_left = sum(second for second in time_line[:mid])

for second in time_line[:mid]:
    if second == 0:
        time_left = time_left * 0.8
    else:
        time_left += second

# time_right = sum(second for second in time_line[mid:])

for second in time_line[:mid:-1]:

    if second == 0:
        time_right = time_right * 0.8
    else:
        time_right += second

if time_left < time_right:
    winner = 'left'
    winner_time = time_left
else:
    winner = 'right'
    winner_time = time_right

print(f'The winner is {winner} with total time: {winner_time:.1f}')
