range_start = int(input())
range_end = int(input())

for first_digit in range(range_start, range_end+1):
    for second_digit in range(range_start, range_end+1):
        for third_digit in range(range_start, range_end+1):
            for fourth_digit in range(range_start, range_end+1):
                if (((first_digit % 2 == 0 and fourth_digit % 2 != 0) or (first_digit % 2 != 0 and fourth_digit % 2 == 0))
                        and first_digit > fourth_digit and (second_digit + third_digit) % 2 == 0):
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')
