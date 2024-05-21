from math import pi

figure = input()

if figure == "square":
    a = float(input())
    print(f"{a ** 2:.3f}")

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    print(f"{a * b:.3f}")

elif figure == "circle":
    r = float(input())
    print(f"{pi * r ** 2:.3f}")

elif figure == "triangle":
    a = float(input())
    h = float(input())
    print(f"{1 / 2 * a * h:.3f}")
