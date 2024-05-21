holidays = int(input())

play_norm = 30000
playtime_workdays = 63
playtime_holidays = 127
work_days = 365 - holidays

year_minutes = 356 * 24 * 60

total_play_workdays = playtime_workdays * work_days
total_play_holidays = playtime_holidays * holidays


total_playtime = total_play_holidays + total_play_workdays

playtime_difference = total_playtime - play_norm

if total_playtime > play_norm:
    print("Tom will run away")
    print(f"{playtime_difference // 60} hours and {playtime_difference % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{(play_norm - total_playtime) // 60} hours and {(play_norm - total_playtime) % 60} minutes less for play")
