"""
    Stwórz klasę o nazwie Rectangle.
    Klasa powinna mieć dwa pola dla boków oraz metodę area do liczenia pola prostokąta.
"""

<<<<<<< HEAD
class Rectangle:
    
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def area(self):
        self.area_of_rectangle = self.side_a * self.side_b
        return self.area_of_rectangle


rec_a = Rectangle(5, 10)

print(rec_a.area())
=======

class Rectangle:
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def get_area(self):
        return self.side_1 * self.side_2


if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print(f"Area of rectangle is {rectangle.get_area()}")
>>>>>>> main
