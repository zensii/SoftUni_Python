def operate(operation: str, *args: int) -> int:
    from functools import reduce

    def sum_args():
        result = sum(args)
        return result
    def subtract_args():
        result = reduce(lambda x, y: x - y, args)
        return result
    def multiply_args():
        result = reduce(lambda x, y: x * y, args)
        return result
    def divide_args():
        if 0 in args[1:]:
            raise ValueError("Division by zero not allowed")
        else:
            result = reduce(lambda x, y: x / y, args)
            return result

    operations = {
        '+': sum_args,
        '-': subtract_args,
        '*': multiply_args,
        '/': divide_args
    }

    return operations[operation]()


print(operate("/", 3, 2))