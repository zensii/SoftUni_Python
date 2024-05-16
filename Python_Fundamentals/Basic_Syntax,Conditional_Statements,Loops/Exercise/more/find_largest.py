number = input()
max_num = list()
number = list(number)

# for i in range(len(number)):
#     max_num.append(max(number))
#     number.remove(max(number))
#
# for char in max_num:
#     print(char, end='')


number.sort(reverse=True)
print(''.join(number))












