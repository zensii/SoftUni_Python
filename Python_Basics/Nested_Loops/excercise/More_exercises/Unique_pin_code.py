upper_limit_1 = int(input())
upper_limit_2 = int(input())
upper_limit_3 = int(input())

for first_digit in range(2, upper_limit_1+1):
    for second_digit in range(1, upper_limit_2+1):
        Is_prime = True
        for divisor in range(2, second_digit):
            if second_digit % divisor == 0:
                Is_prime = False
                break
        for third_digit in range(1, upper_limit_3+1):
            if first_digit % 2 == 0 and 2 <= second_digit <= 7 and third_digit % 2 == 0 and Is_prime:
                print(first_digit, second_digit, third_digit, end='')
                print()
