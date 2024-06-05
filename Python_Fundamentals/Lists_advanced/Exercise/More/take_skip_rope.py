def separate():
    for char in input_string:
        if char.isdigit():
            numbers_list.append(int(char))
        else:
            letters_list.append(char)

    for i in range(len(numbers_list)):
        if i % 2 == 0:
            take_list.append(numbers_list[i])
        else:
            skip_list.append(numbers_list[i])


def combine():
    secret_message = ''
    letters_string = ''.join(letters_list)
    current_index = 0

    for take_position, take_value in enumerate(take_list):
        secret_message += letters_string[current_index:current_index + take_value]
        current_index += take_value
        for skip_position, skip_value in enumerate(skip_list):
            if take_position == skip_position:
                current_index += skip_value
                break
    return secret_message


def main():

    separate()
    secret_message = combine()
    return secret_message


input_string = input()
numbers_list = []
letters_list = []
take_list = []
skip_list = []

print(main())
