def main(number):
    number_list = [int(num) for num in str(number)]

    def sum_even(number_list):
        sum_even = 0
        for number in number_list:
            if number % 2 == 0:
                sum_even += int(number)
        return sum_even

    def sum_odd(number_list):
        sum_odd = 0
        for number in number_list:
            if number % 2!= 0:
                sum_odd += int(number)
        return sum_odd
    return sum_even(number_list), sum_odd(number_list)


number = int(input())

print(f'Odd sum = {main(number)[1]}, Even sum = {main(number)[0]}')
