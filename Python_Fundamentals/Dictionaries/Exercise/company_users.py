def add_employee(user_info, db):
    company, user_id = user_info.split(' -> ')

    if company not in db:
        db[company] = [user_id]
    else:
        if user_id not in db[company]:
            db[company].append(user_id)
    return db


def main():
    database = {}

    while True:
        command = input()
        if command == 'End':
            break
        database = add_employee(command, database)
    for company, users in database.items():
        print(company)
        for employee in users:
            print(f'-- {employee}')


if __name__ == '__main__':
    main()