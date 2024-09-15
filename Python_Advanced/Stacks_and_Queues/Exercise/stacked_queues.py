stack = []
lines = int(input())

for line in range(lines):
    command = input()

    if len(command.split()) == 2:
        stack.append(int(command.split()[1]))
    else:
        if stack:
            match command:
                case '2':
                    stack.pop()
                case '3':
                    print(max(stack))
                case '4':
                    print(min(stack))
r_stack = []
while stack:
    r_stack.append(str(stack.pop()))

print(', '.join(r_stack))
