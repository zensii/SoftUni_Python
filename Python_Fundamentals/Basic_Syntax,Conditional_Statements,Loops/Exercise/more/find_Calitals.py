usr_inp = input()
index_list = []


# for digit_index in range(len(usr_inp)):
#     if usr_inp[digit_index] == usr_inp[digit_index].isupper():
#         index_list.append(digit_index)


for index, digit in enumerate(usr_inp):
    if digit.isupper():
        index_list.append(index)

print(index_list)
