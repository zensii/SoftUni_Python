from collections import deque


def crossing(passing_cars, green_time, yellow_time, crash=False):
    total_passed = 0
    current_green = green_time
    free_window = yellow_time

    while passing_cars and current_green > 0:

        current_car = passing_cars.popleft()
        current_length = len(current_car)

        if current_length <= current_green:
            current_green -= current_length
            total_passed += 1
        elif current_length <= current_green + free_window:
            free_window -= (current_length - current_green)
            current_green = 0
            total_passed += 1
        else:
            remaining_car = current_length - current_green
            current_green = 0
            crash_character = current_car[current_length - remaining_car + free_window]
            print('A crash happened!')
            print(f'{current_car} was hit at {crash_character}.')
            crash = True


    return total_passed, crash


green_time = int(input())
yellow_time = int(input())
waiting_cars = deque()
total_safe = 0
crash_happened = False

while not crash_happened:
    command = input()
    if command == 'END':
        break
    elif command == 'green':
        passed, crash_happened = crossing(waiting_cars, green_time, yellow_time)
        if crash_happened:
            break
        total_safe += passed
    else:
        car = command
        waiting_cars.append(car)

if not crash_happened:
    print('Everyone is safe.')
    print(f'{total_safe} total cars passed the crossroads.')