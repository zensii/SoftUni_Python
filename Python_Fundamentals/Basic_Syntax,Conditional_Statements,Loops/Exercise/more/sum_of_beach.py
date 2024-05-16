usr_inp = input()
usr_inp_lower = usr_inp.lower()
count = 0
words = ['sand', 'water', 'fish', 'sun']

for word in words:
    count += usr_inp_lower.count(word)

print(count)
