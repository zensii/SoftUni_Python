def regiter(database, user, license_plate):
    if user not in database:
        database[user] = license_plate
        print(f'{user} registered {license_plate} successfully')
    else:
        print(f'ERROR: already registered with plate number {database[user]}')


def unregister(user, database):
    if user in database:
        print(f'{user} unregistered successfully')
        del database[user]
    else:
        print(f'ERROR: user {user} not found')



def main():
    database = {}
    n = int(input())
    for i in range(n):
        command = input().split()
        username = command[1]

        if command[0] == 'unregister':
            unregister(username, database)
        else:
            lpn = command[2]
            regiter(database, username, lpn)
    for reg, lpn in database.items():
        print(f'{reg} => {lpn}')


if __name__ == '__main__':
    main()
