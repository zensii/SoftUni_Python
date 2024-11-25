def solution():


    def integers():
        current = 0
        while True:
            current += 1
            yield current


    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        my_l = []
        for i in range(n):
            my_l.append(next(seq))
        return my_l

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
