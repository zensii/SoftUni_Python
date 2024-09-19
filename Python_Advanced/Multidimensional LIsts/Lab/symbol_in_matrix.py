rows = int(input())
matrix = []
found = False
for _ in range(rows):
    matrix.append(list(input()))
target = input()
for i_r, row in enumerate(matrix):
    for i_c, col in enumerate(row):
        if col == target and found == False:
            print(f"({i_r}, {i_c})")
            found = True
if not found:
    print(f"{target} does not occur in the matrix")
