def move(number,coded_message):
    to_move = coded_message[:number]
    coded_message = coded_message[number:] + to_move
    return coded_message


def insert_str(index, value, coded_message):
    coded_message = coded_message[:index] + value + coded_message[index:]
    return coded_message


def change_all(old_string, new_string, coded_message):

    coded_message = coded_message.replace(old_string, new_string)
    return coded_message


def main():

    coded_message = input()
    usr_input = input()

    while usr_input != 'Decode':
        command = usr_input.split('|')

        if command[0] == 'Move':
            coded_message = move(int(command[1]), coded_message)
        if command[0] == 'Insert':
            coded_message = insert_str(int(command[1]), command[2], coded_message)
        if command[0] == 'ChangeAll':
            coded_message = change_all(command[1], command[2], coded_message)
        usr_input = input()

    print(f'The decrypted message is: {coded_message}')


if __name__ == '__main__':
    main()