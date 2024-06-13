# letters = input().split(', ')
# my_dict = {}
# for letter in letters:
#     my_dict[letter] = ord(letter)
# print(my_dict)

print({letter: ord(letter) for letter in input().split(', ')})
