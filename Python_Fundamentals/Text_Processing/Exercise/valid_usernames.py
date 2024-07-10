def check_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def check_contents(username):
    for char in username:
        if char.isalnum() or char == '_' or char == '-':
            continue
        else:
            return False
    return True


def main():
    usr_names = input().split(', ')
    for username in usr_names:
        if check_length(username) and check_contents(username):
            print(username)


if __name__ == '__main__':
    main()
