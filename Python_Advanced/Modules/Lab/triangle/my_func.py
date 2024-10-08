def create_triangle(n: int) -> None:

    for i in range(1, n+1):
        print(*[num for num in range(1, i+1)], sep=' ')
    for j in range(n, 0, -1):
        print(*[num for num in range(1, j)], sep=' ')


if __name__ == '__main__':

    n = int(input('Enter a number: '))
    create_triangle(n)