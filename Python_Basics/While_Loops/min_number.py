text = input()
smallest = float('Inf')

while text != 'Stop':

    number = int(text)

    if number < smallest:
        smallest = number
    text = input()

print(smallest)
