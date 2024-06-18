def collect_user_info(command):
    username = ''
    contest = ''
    points = 0
    username, contest, points = command.split(' -> ')
    points = int(points)
    return username, contest, points


def check_contest(contest, contest_database):
    if contest in contest_database.keys():
        return True
    return False


def check_user_contests(contest, username, contest_database):             # function checks if the user
    if username in contest_database[contest].keys():
        return True
    return False


def check_points(username, contest, points, contest_database):  # function checks if the new points are more than the
                                                                # previous
    if contest_database[contest][username] < points:
        return points
    return contest_database[contest][username]


def collect_usernames(username, username_db):  # function to create a list of unique usernames and set initial value = 0

    if username not in username_db:
        username_db[username] = 0
    return username_db


def track_user_points(usernames_totals, contest_database):  # function to calculate the points of the users and updates
                                                            # the usernames_totals dict.
    for contest, users in contest_database.items():
        for user, points in users.items():
            usernames_totals[user] += points

    return usernames_totals


def sort_users(contests_database):
    sorted_db = {contest: dict(sorted(users_info.items(), key=lambda x: (-x[1], x[0]))) for
                 contest, users_info in contests_database.items()}
    return sorted_db


def main():
    usernames_totals = {}
    contests_db = {}
    command = input()
    sorted_database = {}

    while command != 'no more time':
        student_points = {}
        username, contest, points = collect_user_info(command)
        student_points[username] = points
        usernames_totals = collect_usernames(username, usernames_totals)

        if not check_contest(contest, contests_db):
            contests_db[contest] = student_points

        else:
            if not check_user_contests(contest, username, contests_db):
                contests_db[contest].update(student_points)
            else:
                contests_db[contest][username] = check_points(username, contest, points, contests_db)
        command = input()

    usernames_totals = track_user_points(usernames_totals, contests_db)
    sorted_database = sort_users(contests_db)

    for contest, users in sorted_database.items():
        counter = 1
        print(f'{contest}: {len(users)} participants')
        for user, points in users.items():
            print(f'{counter}. {user} <::> {points}')
            counter += 1
    print('Individual standings:')
    counter = 1
    for user, points in sorted(usernames_totals.items(), key=lambda x: (-x[1], x[0])):
        print(f'{counter}. {user} -> {points}')
        counter += 1


if __name__ == '__main__':
    main()
