class Shape:
    def __init__(self, shir, vys):
        self.shir = shir
        self.vys = vys

class Triangle(Shape):
    def area(self):
        a = (self.shir * self.vys)/2
        return a

class Rectangle(Shape):
    def area(self):
        a = self.shir * self.vys
        return a

a = Triangle(int(input()), int(input()))
b = Rectangle(int(input()), int(input()))
print(a.area())
print(b.area())