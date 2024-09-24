def rectangle(length, width):

    if type(length) == int and type(width) == int:

        def area():
            return width * length

        def perimeter():
            return 2 * (width + length)

        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    else:
        return f"Enter valid values!"


print(rectangle(2, 10))