base_number = int(input())
total = 0

while True:
    number = int(input())
    total += number

    if total >= base_number:
        print(total)
        break

