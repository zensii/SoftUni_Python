stack = []
lines = int(input())

# for line in range(lines):
#     command = input()
#
#     if len(command.split()) == 2:
#         stack.append(int(command.split()[1]))
#     else:
#         if stack:
#             match command:
#                 case '2':
#                     stack.pop()
#                 case '3':
#                     print(max(stack))
#                 case '4':
#                     print(min(stack))
# r_stack = []
# while stack:
#     r_stack.append(str(stack.pop()))
#
# print(', '.join(r_stack))

# alternative advanced solution:

mapper = {
    '1': lambda x: stack.append(int(x)),
    '2': lambda: stack.pop() if stack else None,
    '3': lambda: print(max(stack)) if stack else None,
    '4': lambda: print(min(stack)) if stack else None
}

for line in range(lines):
    command = input().split()
    mapper[command[0]](*command[1:])

print(*reversed(stack), sep=', ')