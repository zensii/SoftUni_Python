def add_stop(index: int, string: str, trip_plan: str):

    if 0 <= index < len(trip_plan):
        trip_plan = trip_plan[:index] + string + trip_plan[index:]
    return trip_plan


def remove_stop(start_index: int, end_index: int, trip_plan: str):

    if 0 <= start_index <= end_index < len(trip_plan):
        trip_plan = trip_plan[:start_index] + trip_plan[end_index+1:]

    return trip_plan


def switch(old_string: str, new_string: str, trip_plan: str):

    if old_string in trip_plan:
        trip_plan = trip_plan.replace(old_string, new_string)

    return trip_plan


def process_commands(commands: list, trip_plan: str):

    for command in commands:
        action, first_variable, second_variable = command.split(':')

        if action == 'Add Stop':
            trip_plan = add_stop(int(first_variable), second_variable, trip_plan)
        elif action == 'Remove Stop':
            trip_plan = remove_stop(int(first_variable), int(second_variable), trip_plan)
        elif action == 'Switch':
            trip_plan = switch(first_variable, second_variable, trip_plan)
        print(trip_plan)
    return trip_plan


stops = input()

commands = []

while True:
    command = input()
    if command == 'Travel':
        break

    else:
        commands.append(command)

trip_plan = process_commands(commands, stops)

print(f'Ready for world tour! Planned stops: {trip_plan}')
