class dictionary_iter:
    def __init__(self, my_dict: dict):
        self.my_dict = my_dict
        self.current = 0

    def __iter__(self):
        return iter(self.my_dict.items())


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
