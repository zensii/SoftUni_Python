size = 4.5


for i in range(size * 2):
    if i <= size:
        spaces = size - i
        stars = i * 2 - 1
    else:
        spaces = i - size
        stars = (size - (i % size)) * 2 - 1
    print("-" * spaces + "*" + "-" * stars + "*" + "-" * spaces)
