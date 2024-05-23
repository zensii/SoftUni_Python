input_string = input().split()
shuffles = int(input())

shuffled = []

for shuffle in range(shuffles):
    first_half = input_string[:len(input_string) // 2]
    second_half = input_string[len(input_string) // 2:]
    shuffled = []

    for index in range(len(first_half)):
        shuffled.append(first_half[index])
        shuffled.append(second_half[index])

    input_string = shuffled

print(shuffled)
