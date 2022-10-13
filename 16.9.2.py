class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.'

    def calc_area(self):
        return self.width * self.height

rect_1 = Rectangle(5, 10, 18, 24)

print(rect_1)
print(rect_1.calc_area())