def math_operations(*args, **kwargs):
    operations = {'a': lambda x,y: x + y,
                  's': lambda x, y: y - x,
                  'd': lambda x, y: y / x if x != 0 else y,
                  'm': lambda x, y: x * y
            }
    for i in range(len(args)):
        operation = list(operations.keys())[i % len(operations)]
        kwargs[operation] = operations[operation](args[i], kwargs[operation])

    final_dict = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    result = ''
    for key, value in final_dict:
        result += f"{key}: {value:.1f}\n"

    return result

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,

d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-

2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))