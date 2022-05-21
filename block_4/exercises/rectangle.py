"""
    Stwórz klasę o nazwie Rectangle.
    Klasa powinna mieć dwa pola dla boków oraz metodę area do liczenia pola prostokąta.
"""

class Rectangle:
    
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def area(self):
        self.area_of_rectangle = self.side_a * self.side_b
        return self.area_of_rectangle


rec_a = Rectangle(5, 10)

print(rec_a.area())
