string_one = input().split(', ')
string_two = input()
final_list = []

for word in string_one:
    if word in string_two:
        final_list.append(word)
print(final_list)