n = int(input())
sum1 = 0
sum2 = 0

for _ in range(n):
    num1 = int(input())
    sum1 += num1
for _ in range(n):
    num2 = int(input())
    sum2 += num2

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    print(f'No, diff = {abs(sum1 - sum2)}')
