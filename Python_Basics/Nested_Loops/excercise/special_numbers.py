N = int(input())

for number in range(1111, 9999):
    string = str(number)
    special = False
    for letter in string:
        digit = int(letter)
        if digit == 0:
            special = False
            break
        if N % digit == 0:
            special = True
        else:
            special = False
            break
    if special:
        print(number, end=" ")
