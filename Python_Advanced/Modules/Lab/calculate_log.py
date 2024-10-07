import math

num = int(input())

try:
    base = int(input())
    result = math.log(num, base)

except ValueError:
    result = math.log(num)

print(f'{result:.2f}')