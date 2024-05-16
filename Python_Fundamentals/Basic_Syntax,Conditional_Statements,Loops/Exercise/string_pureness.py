n = int(input())
unpure = [',', '.', '_']

for _ in range(n):
    pure = True
    string = input()

    for char in string:

        if char in unpure:
            pure = False

    if pure:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
