smaller = int(input())
bigger = int(input())

for num in range(smaller, bigger + 1):
    string = str(num)
    even_sum = 0
    odd_sum = 0
    position = 0
    for index in string:
        position += 1
        if position % 2 == 0:
            even_sum += int(index)
        else:
            odd_sum += int(index)
        continue
    if even_sum == odd_sum:
        print(num, end=' ')

