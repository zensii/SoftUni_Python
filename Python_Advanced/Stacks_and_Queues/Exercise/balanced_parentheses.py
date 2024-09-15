sequence = list(input())
open_pars = ['{', '(', '[']
close_pars = ['}', ')', ']']
stack = []
balanced = True

for parenthesis in sequence:
    if parenthesis in open_pars:
        stack.append(parenthesis)
    else:
        if stack:
            index = open_pars.index(stack[-1])
            if parenthesis == close_pars[index]:
                stack.pop()
            else:
                balanced = False
                break
        else:
            balanced = False

if balanced and not stack:
    print('YES')
else:
    print('NO')