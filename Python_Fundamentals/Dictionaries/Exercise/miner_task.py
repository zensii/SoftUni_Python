def summarize(data_list):
    my_dict = {}
    for i in range(0, len(data_list), 2):
        key = data_list[i]
        value = int(data_list[i+1])
        if i % 2 == 0:
            if key not in my_dict:
                my_dict[key] = value
            else:
                my_dict[key] += value
    return my_dict


command = input()
my_list = []

while True:
    if command == 'stop':
        my_dict = summarize(my_list)
        break
    else:
        my_list.append(command)
    command = input()

for key, value in my_dict.items():
    print(f"{key} -> {value}")

from collections import Counter