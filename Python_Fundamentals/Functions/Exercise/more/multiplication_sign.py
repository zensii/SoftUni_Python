a = int(input())
b = int(input())
c = int(input())


def check_negative(a, b, c):

    checklist = [a, b, c]
    neg_counter = 0
    for num in checklist:
        if num < 0:
            neg_counter += 1
        elif num == 0:
            return print('zero')

    if neg_counter % 2 != 0:
        print('negative')
    else:
        print('positive')


check_negative(a, b, c)