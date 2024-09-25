def separate():

    numbers = list(map(int, input().split()))

    def sum_negative():
        neg_result = sum([neg_num for neg_num in numbers if neg_num < 0])
        print(neg_result)
        return neg_result

    def sum_positive():
        pos_result = sum([pos_num for pos_num in numbers if pos_num > 0])
        print(pos_result)
        return pos_result

    if abs(sum_negative()) > sum_positive():
        return f"The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"

print(separate())