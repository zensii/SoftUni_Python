a = int(input())
b = int(input())
c = int(input())


def add_and_subtract(a,b,c):
    def sum_num(a,b):
        return a + b

    def subtract(sum_num, c):
        return sum_num - c

    return subtract(sum_num(a,b), c)


print(add_and_subtract(a, b, c))
