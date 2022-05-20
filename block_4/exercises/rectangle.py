"""
    Stwórz klasę o nazwie Rectangle.
    Klasa powinna mieć dwa pola dla boków oraz metodę area do liczenia pola prostokąta.
"""


class Rectangle:
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def get_area(self):
        return self.side_1 * self.side_2


if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print(f"Area of rectangle is {rectangle.get_area()}")
