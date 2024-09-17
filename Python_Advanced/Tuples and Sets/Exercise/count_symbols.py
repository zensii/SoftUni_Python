from collections import Counter

letters = Counter(list(input()))
counts = dict(letters)

for letter, count in sorted(counts.items(), key= lambda x: x[0]):
    print(f"{letter}: {count} time/s")