sequence = [num for num in map(int, input().split(' '))]

ordered_sequence = sorted(sequence, reverse=True)
average = sum(sequence) / len(sequence)
final_seq = []

for index in range(len(sequence)):
    if ordered_sequence[index] > average:
        final_seq.append(ordered_sequence[index])

        if len(final_seq) == 5:
            break


if len(final_seq) > 0:
    print(' '.join(num for num in map(str, final_seq)))
else:
    print('No')
