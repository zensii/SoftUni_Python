def calculations(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return 'Cannot divide by zero!'
        else:
            return int(a / b)


operation = input()
a = int(input())
b = int(input())

print(calculations(operation, a, b))