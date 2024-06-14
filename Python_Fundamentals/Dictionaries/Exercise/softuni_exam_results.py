def add_submission(user, language, points, database):

    if user not in database:
        database[user] = {language: int(points)}
    else:
        if language not in database[user]:
            database[user][language] = int(points)
        else:
            if database[user][language] < points:
                database[user][language] = int(points)

    return database


def calculate_user_points(user, database):
    total_points = 0
    if database[user] != 'banned':
        for lang, points in database[user].items():
            total_points += points
    return total_points


def calculate_language_count(language, languages):
    languages[language] += 1


def collect_languages(language, languages):

    if language not in languages:
        languages[language] = 0
    return languages


def ban_user(user, database):
    database[user] = 'banned'


def split_command(command):
    if 'banned' in command:
        user = command.split('-')[0]
        return user, None, None
    else:
        user, language, points = command.split('-')
        points = int(points)

        return user, language, points


def main():
    database = {}
    languages = {}
    while True:
        command = input()

        if command == 'exam finished':
            break
        else:
            user, language, points = split_command(command)
            languages = collect_languages(language, languages)
        if 'banned' in command:
            ban_user(user, database)
        else:
            database = add_submission(user, language, points, database)
            calculate_language_count(language, languages)

    print('Results:')
    for user in database:
        if database[user] != "banned":
            print(f'{user} | {calculate_user_points(user, database)}')
    print('Submissions:')
    for language, submissions in languages.items():
        if language is not None:
            print(f'{language} - {submissions}')


if __name__ == '__main__':
    main()
