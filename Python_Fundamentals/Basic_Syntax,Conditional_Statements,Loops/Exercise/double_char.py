while True:
    string = input()
    if string == 'End':
        break
    if string == 'SoftUni':
        continue
    for letter in string:
        print(2*letter, end='')
    print()
