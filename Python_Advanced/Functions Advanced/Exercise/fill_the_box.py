def fill_the_box(height, length, width, *args):

    args = list(args)
    volume = height * length * width

    for index, cubes in enumerate(args):
        if cubes == 'Finish':
            break
        if volume >= cubes:
            volume -= args[index]
            args[index] = 0
        else:
            args[index] -= volume
            volume = 0
            return f"No more free space! You have {sum(filter(lambda x: isinstance(x, int), args))} more cubes."
    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."


print(fill_the_box(2, 8,

2, 2, 1, 7, 3, 1, 5,

"Finish"))

print(fill_the_box(5, 5,

2, 40, 11, 7, 3, 1, 5,

"Finish"))

print(fill_the_box(10, 10,

10, 40, "Finish", 2, 15,

30))

# import unittest
#
# class Tests(unittest.TestCase):
#     def test(self):
#         result = fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish")
#         self.assertEqual(result, "No more free space! You have 17 more cubes.")
#
# if __name__ == "__main__":
#     unittest.main()