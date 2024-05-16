string_one = input()
string_two = input()
mutate_with = ''
unique = list()

for letter in range(len(string_one)):
    mutate_with += string_two[letter]
    mutated = mutate_with + string_one[letter+1:]
    if mutated not in unique and mutated != string_one:
        unique.append(mutated)
        print(mutated)
