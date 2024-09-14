string = list(input())
open_par = []

for index, char in enumerate(string):
    if char == '(':
        open_par.append(index)
    elif char == ')':
        print(''.join(string[open_par.pop():index+1]))

