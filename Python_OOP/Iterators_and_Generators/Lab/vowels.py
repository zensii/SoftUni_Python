class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = [letter for letter in self.string if letter in 'aeuoyiAEUOYI']
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index < len(self.vowels):
            return self.vowels[self.current_index]
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
