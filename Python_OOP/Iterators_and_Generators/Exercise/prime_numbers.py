def get_primes(num_list: list):
    for num in num_list:
        if isinstance(num, int) and num > 1:
            for divisor in range(2, round(num**0.5)+1):
                if num % divisor == 0:
                    break
            else:
                yield num



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))