input_string = input()
n = int(input())

# def repeat_string(string, n):
#     return string * n
#
#
# print(repeat_string(input_string, n))

repeat_string = lambda a, b: a * b

print(repeat_string(input_string, n))
