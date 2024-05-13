vowels = ['a', 'e', 'i', 'o', 'u', 'y']
power_word = None
power = 0

while True:
    ascii_sum = 0
    user_input = input()
    if user_input == 'End of words':
        break

    word = user_input

    for letter in word:
        ascii_sum += ord(letter)

    if word[0].lower() in vowels:
        ascii_sum = ascii_sum * len(word)
    else:
        ascii_sum = int(ascii_sum / len(word))

    if ascii_sum > power:
        power = ascii_sum
        power_word = word


print(f'The most powerful word is {power_word} - {power}')






