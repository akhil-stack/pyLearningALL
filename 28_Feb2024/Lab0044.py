# Polymorphism

class Shape:
    def Area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


Shape1 = Rectangle(50, 50)
print(Shape1.area())
Shape2= Circle(10)
print(Shape2.area())


