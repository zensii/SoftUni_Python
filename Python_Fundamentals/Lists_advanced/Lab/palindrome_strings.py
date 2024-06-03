list_words = input()
palindrome_word = input()

final_list = [word for word in list_words.split() if word == word[::-1]]

# for word in list_words.split():
#     if word == word[::-1]:
#         final_list.append(word)

occurrences = final_list.count(palindrome_word)

print(final_list)
print(f'Found palindrome {occurrences} times')
