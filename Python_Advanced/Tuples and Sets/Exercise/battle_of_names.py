n = int(input())
even_set = set()
odd_set = set()

for row in range(1, n+1):
    name = input()
    result = sum([ord(char) for char in name]) // row
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(even_set) == sum(odd_set):
    print(', '.join(map(str, even_set.union(odd_set))))
elif sum(odd_set) > sum(even_set):
    print(', '.join(map(str, odd_set.difference(even_set))))
else:
    print(', '.join(map(str,even_set.symmetric_difference(odd_set))))

