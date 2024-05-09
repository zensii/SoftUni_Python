sum_prime = 0
sum_non_prime = 0

while True:
    command = input()
    if command == 'stop':
        print(f'Sum of all prime numbers is: {sum_prime}')
        print(f'Sum of all non prime numbers is: {sum_non_prime}')
        break
    number = int(command)
    if number < 0:
        print('Number is negative.')
        continue
    else:
        counter = 0
        for prime in range(1, number + 1):
            if number % prime == 0:
                counter += 1
        if counter > 2:
            sum_non_prime += number
        else:
            sum_prime += number
