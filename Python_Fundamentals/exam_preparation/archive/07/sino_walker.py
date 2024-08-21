departure_time = input()
steps_count = int(input())
time_per_step = int(input())


def arrival(time, steps, per_step):

    hours, minutes, seconds = departure_time.split(':')
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)

    seconds_to_add = steps_count * time_per_step

    minutes_to_add, seconds = divmod(seconds + seconds_to_add, 60)
    hours_to_add, minutes = divmod(minutes + minutes_to_add, 60)
    _, hours = divmod(hours + hours_to_add, 24)

    return hours, minutes, seconds


hours, minutes, seconds = arrival(departure_time, steps_count, time_per_step)

print(f"Time Arrival: {hours:02}:{minutes:02}:{seconds:02}")
