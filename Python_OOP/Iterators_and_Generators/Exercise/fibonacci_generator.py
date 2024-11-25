def fibonacci():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2

fib_list = []
generator = fibonacci()
for i in range(10):
    fib_list.append(i)
print(' '.join(str(n) for n in fib_list))
