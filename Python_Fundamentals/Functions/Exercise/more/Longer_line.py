from math import floor


def closed_to_center(x1, y1, x2, y2, x3, y3, x4, y4):
    line_one_length = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    line_two_length = ((x4-x3)**2 + (y4-y3)**2) ** 0.5
    x1_zero = (x1**2 + y1**2) ** 0.5
    x2_zero = (x2**2 + y2**2) ** 0.5
    x3_zero = (x3**2 + y3**2) ** 0.5
    x4_zero = (x4**2 + y4**2) ** 0.5

    if line_one_length >= line_two_length:
        if x1_zero <= x2_zero:
            return f'{floor(x1), floor(y1)}{floor(x2), floor(y2)}'
        else:
            return f'{floor(x2), floor(y2)}{floor(x1), floor(y1)}'
    else:
        if x3_zero <= x4_zero:
            return f'{floor(x3), floor(y3)}{floor(x4), floor(y4)}'
        else:
            return f'{floor(x4), floor(y4)}{floor(x3), floor(y3)}'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(closed_to_center(x1, y1, x2, y2, x3, y3, x4, y4))
