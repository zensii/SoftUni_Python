inputs = int(input())
open_brackets = 0
closed_brackets = 0

for inpt in range(inputs):
    entry = input()
    if entry == ')' and open_brackets == 0:
        closed_brackets += 1
        break
    elif entry == ')' and open_brackets == 1:
        open_brackets = 0
        closed_brackets = 0

    elif entry == '(' and open_brackets != 0:
        open_brackets += 1

        break
    elif entry == '(':
        open_brackets += 1

if open_brackets == closed_brackets == 0:
    print(f'BALANCED')
else:
    print(f'UNBALANCED')
