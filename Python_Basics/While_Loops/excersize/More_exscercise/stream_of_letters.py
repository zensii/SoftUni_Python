letters = ''
word = ''
n = 0
o = 0
c = 0

while True:
    entry = input()

    if entry == "End":
        print(word)
        break

    if ('A' <= entry <= 'Z') or ('a' <= entry <= 'z'):
        letter = str(entry)
        if letter == 'n' and n != 1:
            n += 1
        elif letter == 'o' and o != 1:
            o += 1
        elif letter == 'c' and c != 1:
            c += 1
        else:
            letters += letter

    if n == 1 and o == 1 and c == 1:
        letters += ' '
        n = 0
        o = 0
        c = 0
        word = letters
