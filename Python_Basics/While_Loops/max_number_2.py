text = input()
largest = float('-Inf')


while True:

    number = int(text)

    if number > largest:
        largest = number

    text = input()

    if text == 'Stop':
        break

print(largest)
