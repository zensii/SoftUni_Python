class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, new_radius: float):
        self.radius = new_radius

    def get_area(self):
        return round((self.PI * self.radius * self.radius), 2)

    def get_circumference(self):
        return round((self.PI * 2 * self.radius), 2)

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
