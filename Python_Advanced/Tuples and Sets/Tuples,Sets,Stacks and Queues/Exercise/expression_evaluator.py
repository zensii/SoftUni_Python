from collections import deque
import operator
from functools import reduce

string = input().split()

current_calculation = deque()
result = 0

for char in string:

    if char.isnumeric() or len(char) > 1:
        current_calculation.append(int(char))
    else:
        if char == '*':
            result = reduce(operator.mul, current_calculation)
        elif char == '/':
            result = reduce(operator.floordiv, current_calculation)
        elif char == '+':
            result =reduce(operator.add, current_calculation)
        elif char == '-':
            result = reduce(operator.sub, current_calculation)

        current_calculation.clear()
        current_calculation.append(result)

print(*current_calculation)
