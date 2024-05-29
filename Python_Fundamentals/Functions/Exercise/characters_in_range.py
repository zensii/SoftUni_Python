first_char = input()
end_char = input()


def in_between(a, b):
    char_list = []
    for char in range(ord(a)+1, ord(b)):
        char_list.append(chr(char))
    return ' '.join(char_list)


print(in_between(first_char, end_char))
