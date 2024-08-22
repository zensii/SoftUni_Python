def collect_inputs():
    lines = []
    while True:
        usr_input = input()

        if usr_input == 'stop playing':
            break
        list_line = list(map(int, usr_input.split()))
        lines.append(list_line)
    return lines


def check_unique(line):

    set_line = set(line)
    unique = len(line) == len(set_line)
    return unique


def get_output(line):

    return sum(line) / len(line)


def modify_string(line, unique):
    if unique:
        return list(sorted(map(lambda x: x + 2 if x % 2 == 0 else x, line)))
    else:
        return list(sorted(map(lambda x: x+3 if x % 2 != 0 else x, line)))


lines = collect_inputs()

for line in lines:
    unique = check_unique(line)
    modified_string = modify_string(line, unique)
    output = get_output(modified_string)

    if unique:
        print(f"Unique list: {','.join(map(str, modified_string))}")
    else:
        print(f"Non-unique list: {':'.join(map(str, modified_string))}")
    print(f"Output: {output:.2f}")
