n = int(input())

if n % 2 == 0:
    odd = 0
else:
    odd = 1

for i in range((n//2) + odd):
    left_right = (n - 1) // 2 - i
    mid = n - 2 * left_right - 2
    if mid >= 0:
        print(left_right * '-' + '*' + mid * '-' + '*' + left_right * '-')
    else:
        print(left_right * '-' + mid * '-' + '*' + left_right * '-')

for j in range(1, n//2 + odd):
    mid = n - 2 * j - 2
    if mid >= 0:
        print(j*'-' + '*' + mid*'-' + '*' + j*'-')
    else:
        print(j*'-' + mid*'-' + '*' + j*'-')
