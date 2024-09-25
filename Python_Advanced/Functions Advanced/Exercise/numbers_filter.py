def even_odd_filter(even=None , odd=None ):
    my_dict = {}
    if even:
        my_dict['even'] = [even_num for even_num in even if even_num % 2 == 0]
    if odd:
        my_dict['odd'] = [odd_num for odd_num in odd if odd_num % 2 != 0]

    return dict(sorted(my_dict.items() , key= lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))