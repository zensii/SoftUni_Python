second_digit = int(input())
prime = True

for divisor in range(2, second_digit):
    if second_digit % divisor == 0:
        Is_prime = False
        print(second_digit, 'is not prime')
        break
else:
    print(second_digit, 'is prime')
