n = int(input())

if n % 2 == 0:
    first_star = 2
else:
    first_star = 1

for i in range(0, n, 2):
    print(((n-first_star-i)//2) * '-' + (i + first_star) * '*' + ((n-first_star-i)//2) * '-')
for j in range(n//2):
    print('|' + (n - 2) * '*' + '|')

