def multiply(*args):
    from functools import reduce
    return reduce(lambda x, y: x * y, args)
