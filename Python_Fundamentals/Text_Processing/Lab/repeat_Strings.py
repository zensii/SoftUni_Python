def multiply_string(string):
    length = len(string)
    return string * length


def main():
    usr_input = input().split()
    result_string = ''
    for string in usr_input:
        result_string += multiply_string(string)
    print(result_string)


if __name__ == '__main__':
    main()
