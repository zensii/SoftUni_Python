# n = int(input())
#
# for x in range(n):
#     if x == 0 or x == n-1:
#         print('+ '+(n-2)*'- '+'+')
#     else:
#         print('| '+(n-2)*'- '+'|')

n = int(input())


print('+ ' + (n - 2) * '- ' + '+')
for y in range(n-2):
    print('| '+(n-2)*'- '+'|')
print('+ ' + (n - 2) * '- ' + '+')
