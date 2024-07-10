def reverse_string(string):
    return string[::-1]


def main():
    usr_input = input()
    while usr_input != 'end':
        print(f'{usr_input} = {reverse_string(usr_input)}')
        usr_input = input()


if __name__ == '__main__':
    main()
