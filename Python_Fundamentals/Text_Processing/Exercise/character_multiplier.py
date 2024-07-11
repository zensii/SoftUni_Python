# def multiply_strings(first: str, second: str):
#     total = 0
#     if len(first) <= len(second):
#         for index in range(len(first)):
#             total += ord(first[index]) * ord(second[index])
#         for char in second[len(first):]:
#             total += ord(char)
#     else:
#         for index in range(len(second)):
#             total += ord(second[index]) * ord(first[index])
#         for char in first[len(second):]:
#             total += ord(char)
#
#     return total


def zipping(first, second):
    zipped_list = zip(first, second)
    return zipped_list


def multiply(zipped_list):
    total = 0
    for a, b in zipped_list:
        total += ord(a) * ord(b)
    return total


def add_remaining(first, second):
    remains = 0
    if len(first) >= len(second):
        for char in first[len(second):]:
            remains += ord(char)
    else:
        for char in second[len(first):]:
            remains += ord(char)
    return remains


two_strings = input().split()
first, second = two_strings

# print(multiply_strings(first, second))

total = multiply(zipping(first, second))
total += add_remaining(first, second)

print(total)
