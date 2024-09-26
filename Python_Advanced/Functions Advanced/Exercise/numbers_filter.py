def even_odd_filter(**kwargs):

    if 'even' in kwargs:
        kwargs['even'] = [even_num for even_num in kwargs['even'] if even_num % 2 == 0]
    if 'odd' in kwargs:
        kwargs['odd'] = [odd_num for odd_num in kwargs['odd'] if odd_num % 2 != 0]

    # an alternative solution using dict comprehension
    # kwargs = {key: [ x for x in numbers if x%2 == ( 0 if key == 'even' else 1)] for key, numbers in kwargs.items()}

    return dict(sorted(kwargs.items() , key= lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))