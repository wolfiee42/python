from abc import ABC , abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius * 3.14


class Square(Shape):
    
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2


class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Pizza(Circle):
    
    def __init__(self, radius, toppings):
        super().__init__(radius)
        self.toppings = toppings
    
        

shapes = [Circle(4), Square(5), Rectangle(6, 7), Pizza(4, "chesse")]

for shape in shapes:
    print(f" {shape.area()} cm^2")