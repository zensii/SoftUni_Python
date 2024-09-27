def grocery_store(**kwargs):

    result = ''
    sorted_names = dict(sorted(kwargs.items(), key=lambda x: (-len(x[0]), x)))
    sorted_dict = dict(sorted(sorted_names.items(), key=lambda x: (-x[1])))
    for key, value in sorted_dict.items():
        result += f"{key}: {value}\n"
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    basta=2,
    eggs=20,
    carrot=1,
))