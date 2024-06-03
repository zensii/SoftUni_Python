list_todo = []
sorted_list = []
final_list = []
while True:
    command = input()
    if command == "End":
        break

    list_todo.append(command.split('-'))
#
# for item in list_todo:
#     item[0] = int(item[0])

sorted_list = sorted(list_todo, key=lambda x: int(x[0]))
final_list = [item[1] for item in sorted_list]

# for item in sorted_list:
#     final_list.append(item[1])

print(final_list)
