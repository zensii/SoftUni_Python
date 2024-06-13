entries = int(input())
words = [input() for _ in range(entries*2)]
my_dict = {}

for index in range(0, len(words), 2):
    if words[index] not in my_dict:
        my_dict[words[index]] = [words[index+1]]
    else:
        my_dict[words[index]].append(words[index+1])

for key, value in my_dict.items():
    print(f"{key} - {', '.join(value)}")
