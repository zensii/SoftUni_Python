def perfect_checker(integer):
    sum_of_divisors = 0
    for i in range(1, integer):
        if integer % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == integer:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


integer = int(input())
perfect_checker(integer)
