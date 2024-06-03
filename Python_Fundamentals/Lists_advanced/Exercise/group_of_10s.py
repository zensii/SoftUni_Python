input_list = list(map(int, input().split(', ')))
biggest = max(input_list)
number_of_groups = biggest//10 if biggest % 10 == 0 else biggest//10+1
group_range = 0
current_group_list = []

for group in range(number_of_groups):
    group_range += 10
    current_group_list.clear()
    for number in input_list[::-1]:
        if number <= group_range:
            current_group_list.append(number)
            input_list.remove(number)
    print(f"Group of {group_range}'s: {current_group_list[::-1]}")
