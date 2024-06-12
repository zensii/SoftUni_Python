my_list = input().split()
my_dict = {}

for item in range(0, len(my_list), 2):

    my_dict[my_list[item]] = int(my_list[item+1])

print(my_dict)