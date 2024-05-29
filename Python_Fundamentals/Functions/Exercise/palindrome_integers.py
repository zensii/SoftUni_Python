input_list = [num for num in input().split(', ')]


def check_palindrome(input_list):
    for number in input_list:
        if number == number[::-1]:
            print(True)
        else:
            print(False)


check_palindrome(input_list)