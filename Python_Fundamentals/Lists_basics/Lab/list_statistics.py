n = int(input())
positive = []
negative = []

for entry in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)

    else:
        negative.append(number)

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}\n Sum of negatives: {sum(negative)}')