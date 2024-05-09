n = int(input())
sum_num = 0

for _ in range(n):
    number = int(input())
    sum_num += number
print(f'{sum_num / n:.2f}')
