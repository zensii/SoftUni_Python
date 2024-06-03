list_names = input().split(', ')

# modified_list = []

# for name in list_names:
#     name_length = len(name)
#     name_length_tuple = (name, name_length)
#     modified_list.append(name_length_tuple)
#
# sorted_list = [item[0] for item in sorted(modified_list, key=lambda x: (-x[1], x[0]))]

sorted_list = sorted(list_names, key=lambda x: (-len(x), x))  # shorted version of the above

print(sorted_list)

# one line:
# print(sorted(input().split(', '), key=lambda x: (-len(x), x)))
