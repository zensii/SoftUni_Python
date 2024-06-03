# num_list = list(map(int, input().split(', ')))
# #
# # for i in range(len(num_list)):
# #     if int(num_list[i]) % 2 == 0:
# #         even_list.append(i)
#
# even_list = [i for i in range(len(num_list)) if (num_list[i]) % 2 == 0]
#
# print(even_list)



num_list = list(map(int, input().split(', ')))

even_list = filter(lambda x: num_list[x] % 2 == 0, range(len(num_list)))

print(list(even_list))
