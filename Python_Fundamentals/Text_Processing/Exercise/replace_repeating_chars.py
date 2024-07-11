input_string = input()

# for index in range(len(input_string) - 1, 0, -1):
#     if input_string[index] == input_string[index-1]:
#         del input_string[index-1]

result_list = [input_string[0]]
for char in input_string[1:]:
    if char != result_list[-1]:
        result_list.append(char)

print(''.join(result_list))