first_char = input()
second_char = input()
string = input()
result = 0
first_index = ord(first_char)
second_index = ord(second_char)

for char in string:
    if first_index < ord(char) < second_index:
        result += ord(char)

print(result)

