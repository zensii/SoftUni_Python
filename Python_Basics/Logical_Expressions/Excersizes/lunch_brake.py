from math import ceil

soap_opera = input()
episode_length = int(input())
time_brake = int(input())

lunch_time = time_brake / 8
relax_time = time_brake / 4
movie_time = time_brake - (lunch_time + relax_time)

if movie_time >= episode_length:
    print(f"You have enough time to watch {soap_opera} "
          f"and left with {ceil(movie_time - episode_length)} minutes free time.")

else:
    print(f"You don't have enough time to watch {soap_opera},"
          f" you need {ceil(episode_length - movie_time)} more minutes.")
