def check_operation(command, database):

    if '|' in command:
        database = add_force_user(command, database)
    elif '->' in command:
        database = switch_side(command, database)

    return database


def check_force_user(database, user):
    for force_side, user_names in database.items():
        if user in user_names:
            return True
    return False


def add_force_user(command, database):
    force_side, user_name = command.split(' | ')
    if not check_force_user(database, user_name):
        if force_side not in database:
            database[force_side] = [user_name]
        else:
            database[force_side].append(user_name)
    return database


def find_key(database,user_name):
    for force_side, user_names in database.items():
        if user_name in user_names:
            return force_side


def switch_side(command, database):
    user_name, force_side = command.split(' -> ')
    if check_force_user(database, user_name):
        key = find_key(database, user_name)
        del database[key][database[key].index(user_name)]
    if force_side not in database.keys():
        database[force_side] = [user_name]
    else:
        database[force_side].append(user_name)
    print(f'{user_name} joins the {force_side} side!')

    return database


def main():
    force_database = {}

    while True:
        command = input()
        if command == 'Lumpawaroo':
            break

        force_database = check_operation(command, force_database)

    for side, users in force_database.items():
        if len(force_database[side]) != 0:
            print(f'Side: {side}, Members: {len(force_database[side])}')
            for user in users:
                print(f'! {user}')


if __name__ == '__main__':
    main()
    