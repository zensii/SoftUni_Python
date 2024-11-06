class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        from math import floor
        if type(float_value) == float:
            return Integer(floor(float_value))
        return f"value is not a float"

    @classmethod
    def from_roman(cls, value: str):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        specials = {'IV': 4, 'IX': 9, 'XL': 40, 'XC':90, 'CD': 400, 'CM': 900}

        result = 0
        index = 0
        while index < len(value):
            current_symbol = value[index]
            try:
                next_symbol = value[index+1]
            except IndexError:
                next_symbol = ''
            try:
                result += specials[current_symbol+next_symbol]
                index += 2
            except KeyError:
                result += roman_dict[value[index]]
                index += 1
        return Integer(result)

    @classmethod
    def from_string(cls, value: str):
        if type(value) == str:
            return Integer(int(value))
        else:
             return 'wrong type'



first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))



