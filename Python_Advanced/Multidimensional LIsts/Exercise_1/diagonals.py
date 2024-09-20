n = int(input())
matrix = [list(map(int, input().split(', '))) for row in range(n)]

main_diag = []
sec_diag = []

for index in range(n):
    main_diag.append(matrix[index][index])
    sec_diag.append(matrix[index][n - (index + 1)])

print(f"Primary diagonal: {', '.join(str(el) for el in main_diag)}. Sum: {sum(main_diag)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in sec_diag)}. Sum: {sum(sec_diag)}")
