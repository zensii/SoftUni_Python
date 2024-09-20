n = int(input())
matrix = [list(map(int, input().split())) for row in range(n)]

main_diag = []
sec_diag = []

for index in range(n):
    main_diag.append(matrix[index][index])
    sec_diag.append(matrix[index][n - (index + 1)])

print(abs(sum(main_diag) - sum(sec_diag)))
