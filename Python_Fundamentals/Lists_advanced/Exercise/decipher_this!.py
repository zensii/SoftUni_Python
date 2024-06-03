coded_message = input().split()
decoded_word = ''
decoded_message = []

for word in coded_message:
    digits = ''
    chars = []
    for char in word:
        if char.isdigit():
            digits += char
        else:
            chars.append(char)

    first_character = chr(int(digits))
    chars[0], chars[-1] = chars[-1], chars[0]
    decoded_word = first_character + ''.join(chars)
    decoded_message.append(decoded_word)

print(' '.join(decoded_message))
