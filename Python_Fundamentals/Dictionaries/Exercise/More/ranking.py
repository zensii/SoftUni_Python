def collect_contests():
    contests = {}
    command = input()
    while command != 'end of contests':
        contest_name, contest_password = command.split(':')
        contests[contest_name] = contest_password
        command = input()
    return contests


def check_validity(contests, contest, password):
    if contest in contests.keys() and contests[contest] == password:
        return True
    return False


def sum_points(user_data):
    best_user = 0
    best_score = 0

    for user, user_contest_data in user_data.items():
        user_score = 0
        for contest, points in user_contest_data.items():
            user_score += points
            if user_score > best_score:
                best_user = user
                best_score = user_score
    return best_user, best_score


def sort_dict(user_data):
    # first sort by the values of the contests in the inner dictionary
    sorted_dict = {name: dict(sorted(inner_dict.items(), key=lambda x: x[1], reverse=True)) for name, inner_dict in
                   user_data.items()}
    # then sort by the keys of the outer dictionary
    final_sorted = dict(sorted(sorted_dict.items(), key=lambda x: x[0]))

    return final_sorted


def main():

    user_data = {}
    contests = collect_contests()  # create db with contests and its password
    command = input()
    while command != 'end of submissions':
        contest, password, username, points = command.split('=>')
        points = int(points)
        user_points = {}
        if check_validity(contests, contest, password):  # if contest is valid
            user_points[contest] = points
            if username not in user_data.keys():  # if user not present already:
                user_data[username] = user_points
            else:  # if user is in db:
                if contest not in user_data[username].keys():  # check if user attended the same contest already:
                    user_data[username].update(user_points)  # if not add the points for this contest to the user data
                else:
                    if user_data[username][contest] < points:    # if yes, check if new points are more than the old
                        user_data[username][contest] = points    # and if yes add them.
        command = input()

    sorted_dict = sort_dict(user_data)

    best_user, best_score = sum_points(user_data)
    print(f'Best candidate is {best_user} with total {best_score} points.')
    print('Ranking:')
    for user, user_contest_data in sorted_dict.items():
        print(user)
        for contest, points in user_contest_data.items():
            print(f'#  {contest} -> {points}')


if __name__ == '__main__':
    main()
