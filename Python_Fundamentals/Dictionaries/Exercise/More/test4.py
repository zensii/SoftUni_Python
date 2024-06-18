user = input()
len_user = len(user)
command = input().split()


while command[0] != "Registration":
    substring = ''
    if command[0] == 'Letters' and command[1] == 'Lower':
        user = user.lower()
        print(user)

    elif command[0] == 'Letters' and command[1] == 'Upper':
        user = user.upper()
        print(user)

    elif command[0] == 'Reverse':
        start = int(command[1])
        end = int(command[2])
        if (0 <= start < len_user) and (0 < end < len_user) and (start < end):
            substring = user[start:end+1][::-1]
            print(substring)

    elif command[0] == 'Substring':
        if command[1] not in user:
            print(f"The username {user} doesn't contain {command[1]}.")
        else:
            user = user.replace(command[1], '')
            print(user)

    elif command[0] == 'Replace':
        if command[1] in user:
            user = user.replace(command[1], '-')
        print(user)

    elif command[0] == 'IsValid':
        if command[1] in user:
            print("Valid username.")
        else:
            print(f"{command[1]} must be contained in your username.")

    command = input().split()
