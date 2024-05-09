n = int(input())

for num in range(n+1):
    if num % 2 == 0:
        num = 2 ** num
        print(num)
