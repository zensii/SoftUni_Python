array = list(map(int, input().split()))

result = 0

for number in array:
    result = result ^ number

print(result)

