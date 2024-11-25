class countdown_iterator:
    def __init__(self, count):
        self.current = - 1
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.count:
            raise StopIteration
        self.current += 1
        return self.count - self.current


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
