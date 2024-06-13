input_string = input()
dict_counts = {}
for char in input_string:
    if char not in dict_counts and char != ' ':
        dict_counts[char] = 1
    elif char in dict_counts and char != ' ':
        dict_counts[char] += 1

for key, value in dict_counts.items():
    print(f'{key} -> {value}')
