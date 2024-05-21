N1 = int(input())
N2 = int(input())
operator = input()

result = 0
number_type = ''  # even/odd

if operator == '+':
    result = N1 + N2
    if result % 2 == 0:
        number_type = 'even'
    else:
        number_type = 'odd'
    print(f'{N1} {operator} {N2} = {result} - {number_type}')

elif operator == '-':
    result = N1 - N2
    if result % 2 == 0:
        number_type = 'even'
    else:
        number_type = 'odd'
    print(f'{N1} {operator} {N2} = {result} - {number_type}')

elif operator == '*':
    result = N1 * N2
    if result % 2 == 0:
        number_type = 'even'
    else:
        number_type = 'odd'
    print(f'{N1} {operator} {N2} = {result} - {number_type}')

elif operator == '/' and not N2 == 0:
    result = N1 / N2
    print(f'{N1} / {N2} = {result:.2f}')

elif operator == '%' and not N2 == 0:
    result = N1 % N2
    print(f'{N1} % {N2} = {result}')

else:
    print(f'Cannot divide {N1} by zero')
