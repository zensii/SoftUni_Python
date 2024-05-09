text = input()

total = 0

for letter in text:
    if letter == 'a':
        total = total + 1
    elif letter == 'e':
        total = total + 2
    elif letter == 'i':
        total = total + 3
    elif letter == 'o':
        total = total + 4
    elif letter == 'u':
        total = total + 5

print(total)

