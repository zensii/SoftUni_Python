text = input()
repeat = input()

try:
    repeat = int(repeat)
    print(repeat*text)
except ValueError:
    print("Variable times must be an integer")