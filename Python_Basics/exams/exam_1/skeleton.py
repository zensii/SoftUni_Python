minute_ctrl = int(input())
second_ctrl = int(input())
track_length = float(input())
seconds_per_100m = int(input())

quota = minute_ctrl * 60 + second_ctrl
delays = track_length / 120
martin_time = (track_length / 100) * seconds_per_100m - delays * 2.5

if martin_time <= quota:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {martin_time:.3f}.')
else:
    print(f'No, Marin failed! He was {abs(quota - martin_time):.3f} second slower.')
