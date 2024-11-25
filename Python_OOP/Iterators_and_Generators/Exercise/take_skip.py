class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0 - self.step
        self.current_step = 0

    def __iter__(self):
        return self

    def __next__(self):

        self.current_step += 1
        self.current += self.step

        if self.current_step <= self.count:
            return self.current
        else:
            raise StopIteration



numbers = take_skip(2, 6)
for number in numbers:
    print(number)
