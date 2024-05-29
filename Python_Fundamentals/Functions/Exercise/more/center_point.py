from math import floor


def closed_to_center(x1, y1, x2, y2):
    if x1**2 + y1**2 <= x2**2 + y2**2:
        return f'{floor(x1), floor(y1)}'
    else:
        return f'{floor(x2), floor(y2)}'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closed_to_center(x1, y1, x2, y2))
