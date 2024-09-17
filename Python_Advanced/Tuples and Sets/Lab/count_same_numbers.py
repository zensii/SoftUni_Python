sequence = tuple(map(float, input().split()))
printed = []
for item in sequence:
    print(f'{item:.1f} - {sequence.count(item)} times') if item not in printed else None
    printed.append(item)