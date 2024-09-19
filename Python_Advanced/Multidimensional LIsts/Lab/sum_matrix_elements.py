matrix = [[int(el) for el in input().split(', ')] for row in range(int(input().split(', ')[0]))]
tot_sum = sum(sum(el) for el in matrix)

print(tot_sum)
print(matrix)
