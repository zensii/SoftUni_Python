def tribonacci_seq(number):

    tribonacci = []
    if number == 1:
        tribonacci = [1]
    elif number == 2:
        tribonacci = [1, 1]
    elif number == 3:
        tribonacci = [1, 1, 2]
    else:
        tribonacci = [1, 1, 2]
        for i in range(number-3):
            tribonacci.append(sum(tribonacci[i:]))
    for num in tribonacci:
        print(num, end=' ')


number = int(input())
tribonacci_seq(number)
