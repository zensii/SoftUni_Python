n = int(input())

if n % 2 == 0:
    bar = n/2
else:
    bar = n//2+1

for i in range(1, n+1):

    if i == 1 or i == n:
        print(2 * n * '*' + n * ' ' + 2 * n * '*')
    elif i == bar:
        print('*' + ((n * 2)-2) * '/' + '*' + n * '|' + '*' + ((n * 2)-2) * '/' + '*')

    else:
        print('*' + ((n * 2) - 2) * '/' + '*' + n * ' ' + '*' + ((n * 2) - 2) * '/' + '*')
