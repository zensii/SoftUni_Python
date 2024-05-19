sum_ascii = 0
lines = int(input())
for chars in range(lines):
    sum_ascii += ord(input())
print(f'The sum equals: {sum_ascii}')
