def upper_lower(username, command):
    if command == 'Upper':
        username = username.upper()
    elif command == 'Lower':
        username = username.lower()
    print(username)
    return username


def reverse(username, start, end):

    if check_indexes(start, end, len(username)):
        cut_part = username[start:end+1][::-1]
        print(cut_part)


def check_indexes(start, end, length):
    if 0 <= start < length and 0 <= end < length and start < end:
        return True
    return False


def substring(username, sub_string):
    if sub_string in username:
        username = username.replace(sub_string, '')
        print(username)
    else:
        print(f"The username {username} doesn't contain {sub_string}.")
    return username


def replace(username, char):
    if char in username:
        username = username.replace(char, '-')
        print(username)
    return username


def isvalid(username, char):
    if char in username:
        print('Valid username.')
    else:
        print(f'{char} must be contained in your username.')


def main():
    username = input()
    command = input()

    while command != 'Registration':

        command = command.split()

        if command[0] == 'Letters':
            username = upper_lower(username, command[1])

        elif command[0] == 'Reverse':
            start_index = int(command[1])
            end_index = int(command[2])
            reverse(username, start_index, end_index)

        elif command[0] == 'Substring':
            sub_string = command[1]
            username = substring(username, sub_string)

        elif command[0] == 'Replace':
            char = command[1]
            username = replace(username, char)

        elif command[0] == 'IsValid':
            char = command[1]
            isvalid(username, char)

        command = input()


if __name__ == '__main__':
    main()
