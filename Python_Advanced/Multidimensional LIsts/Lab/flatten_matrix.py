rows = int(input())
matrix = []
flattened = []
for _ in range(rows):
    lst = [int(el) for el in input().split(', ')]
    matrix.append(lst)

for row in matrix:
    for el in row:
        flattened.append(el)

print(flattened)

