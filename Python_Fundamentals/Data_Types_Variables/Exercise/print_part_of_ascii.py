range_start = int(input())
range_end = int(input())

for position in range(range_start, range_end+1):
    print(chr(position), end=' ')
