number = int(input()) + 1

while len(str(number)) != len(set(str(number))):
    number += 1

print(number)
