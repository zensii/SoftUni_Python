def age_assignment(*args, **kwargs):
    result = ''
    result_dict = {}
    for name in args:
        result_dict[name] = kwargs[name[0]]
    for name, age in sorted(result_dict.items(), key=lambda x: x[0]):
        result += F"{name} is {age} years old.\n"
    return result

print(age_assignment("Amy", "Bill", "Willy", W=36,

A=22, B=61))

print(age_assignment("Peter", "George", G=26, P=19))