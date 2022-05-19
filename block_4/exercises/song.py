

class Rectangle:
    def __init__(self, bokA, bokB):
        self.bokA = bokA
        self.bokB = bokB

    def area(self):
        area = self.bokA * self.bokB
        return area

rectangle = Rectangle(5, 4)

print(rectangle.area())