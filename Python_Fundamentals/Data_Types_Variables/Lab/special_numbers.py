n = int(input())
special_sum = [5, 7, 11]

for num in range(1, n+1):
    is_special = False
    sum_digits = 0

    for digit in str(num):
        sum_digits += int(digit)
        if sum_digits in special_sum:
            is_special = True
    print(num, '->', is_special)

