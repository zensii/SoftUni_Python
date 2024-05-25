string_list = input().split(', ')
string_integers = [int(digit) for digit in string_list]
removed_counter = 0

while 0 in string_integers:
    string_integers.remove(0)
    removed_counter += 1
for num in range(removed_counter):
    string_integers.append(0)

print(string_integers)
