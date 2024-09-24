def sorting_cheeses(**kwargs):
    for key, items in kwargs.items():
        kwargs[key] = sorted(items, reverse=True)
    sorted_kwargs = (sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''
    for tup in sorted_kwargs:
        result += tup[0] + '\n'
        for item in tup[1]:
            result += str(item) + '\n'

    return result



print(sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    ))
