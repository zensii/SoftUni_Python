

def merge(start_index, end_index):
    merged_string = ''
    modified_string = ''
    for i in range(start_index, end_index+1):
        if i < len(input_string):
            merged_string += input_string[i]
    if merged_string != '':
        input_string[start_index:end_index+1] = [merged_string]
        for charset in input_string:
            modified_string += charset+' '
    return modified_string


def divide(index, parts):





input_string = input().split()

while True:
    command  = input().split()
    if command[0] == '3:1':
        break

    if command[0] == 'merge':
        modified_list = merge(int(command[1]), int(command[2]))
    elif command[0] == 'divide':
        modified_list = divide(int(command[1]), (int(command[2])))

for item in modified_list:
    print(item, end=' ')