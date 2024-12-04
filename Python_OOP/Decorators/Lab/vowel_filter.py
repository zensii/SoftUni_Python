def vowel_filter(function):

    def wrapper():

        vowels = ['a','e','i', 'o', 'u', 'y']
        return [v for v in function() if v in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
