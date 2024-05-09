first_pair = int(input())
second_pair = int(input())
first_pair_number = int(input())
second_pair_number = int(input())

for first_double in range(first_pair, first_pair + first_pair_number+1):

    first_is_prime = True
    for first_divisor in range(2, first_double):
        if first_double % first_divisor == 0:
            first_is_prime = False
            break

    for second_double in range(second_pair, second_pair + second_pair_number+1):

        second_is_prime = True
        for second_divisor in range(2, second_double):
            if second_double % second_divisor == 0:
                second_is_prime = False
                break

        if first_is_prime and second_is_prime:
            print(f'{first_double}{second_double}')
