def concatenate(*args, **kwargs):

    strings = ''.join(args)
    for key, value in kwargs.items():
        if key in strings:
            strings = strings.replace(key, value)

    return strings

print(concatenate("Soft", "UNI", "Is", "Grate", "!",

UNI="Uni", Grate="Great"))