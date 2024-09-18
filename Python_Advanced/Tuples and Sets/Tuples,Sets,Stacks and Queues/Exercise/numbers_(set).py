seq_one = set(map(int, input().split()))
seq_two = set(map(int, input().split()))

commands = {
    'Add First': lambda x, y, z: x.update(z),
    'Add Second': lambda x, y, z: y.update(z),
    'Remove First': lambda x, y, z: x.difference_update(z),
    'Remove Second': lambda x, y, z: y.difference_update(z),
    'Check Subset': lambda x, y, z: print('True') if x.issubset(y) or y.issubset(x) else print('False')

}

n = int(input())

for _ in range(n):
    entry = input().split()
    nums = map(int, entry[2:])
    command = entry[:2]

    commands[' '.join(command)](seq_one, seq_two, nums)


print(*sorted(seq_one), sep=', ')
print(*sorted(seq_two), sep=', ')