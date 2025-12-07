class Shape:
    
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"this is {self.color} and it is {"filled" if self.is_filled is True else "not filled"} ")


class Circle(Shape):
    
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"it is a circle with the area of {3.14 * self.radius * self.radius}")


class Square(Shape):
    
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


class Rectangle(Shape):
    
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 5)
square = Square("blue", False, 5)
rectangle = Rectangle("red", True, 5, 4)

circle.describe()