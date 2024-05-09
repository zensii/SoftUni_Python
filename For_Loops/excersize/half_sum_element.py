n = int(input())
total = 0
max_num = float('-inf')  # minus infinity declaration

for _ in range(1, n+1):
    num = int(input())

    if num > max_num:
        max_num = num
    total += num
if max_num == total - max_num:
    print('Yes')
    print(f'Sum = {total - max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - (total - max_num))}')
