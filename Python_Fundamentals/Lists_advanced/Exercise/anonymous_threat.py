def merge(string, start_index, end_index):

    start_index = int(start_index)
    end_index = int(end_index)
    current_list = string.split()

    if start_index < 0:
        start_index = 0
    if end_index > len(current_list)-1:
        end_index = len(current_list)-1

    merged_string = ''.join(current_list[start_index:end_index+1])
    current_list[start_index:end_index+1] = [merged_string]

    string = ' '.join(current_list)

    return string


def divide_equal(string, index, partitions):
    new_list = []

    current_list = string.split()

    string_to_split = current_list[int(index)]
    length_of_string = len(string_to_split)
    partitions = int(partitions)
    partition_length = length_of_string // int(partitions)

    for i in range(0, length_of_string, partition_length):
        new_list.append(string_to_split[i:i+partition_length])
    joined_string = ' '.join(new_list)
    current_list[int(index)] = joined_string
    string = ' '.join(current_list)

    return string


def divide_unequal(string, index, partitions):
    new_list = []

    current_list = string.split()
    string_to_split = current_list[int(index)]
    length_of_string = len(string_to_split)
    partition_length = length_of_string // int(partitions)

    for i in range(int(partitions)-1):
        new_list.append(string_to_split[i*partition_length:(i+1)*partition_length])

    remainder = string_to_split[len(new_list)*partition_length:]
    new_list.append(remainder)

    joined_string = ' '.join(new_list)
    current_list[int(index)] = joined_string
    string = ' '.join(current_list)
    return string


main_string = input()

while True:
    command = input().split()
    if command[0] == '3:1':
        break
    elif command[0] == 'merge':
        main_string = merge(main_string, command[1], command[2])
    elif command[0] == 'divide':
        if len(main_string.split()[int(command[1])]) % int(command[2]) == 0:
            main_string = divide_equal(main_string, command[1], command[2])
        else:
            main_string = divide_unequal(main_string, command[1], command[2])
print(main_string)