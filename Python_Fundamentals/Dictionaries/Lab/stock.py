my_list = input().split()
needed_product = input().split()
my_dict = {}

for i in range(0, len(my_list), 2):
    key = my_list[i]
    value = int(my_list[i+1])
    my_dict[key] = value

for item in needed_product:
    if item in my_dict:
        print(f'We have {my_dict[item]} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")
        