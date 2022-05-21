"""
Stwórz klasę Polygon, która będzie reprezentować wielokąt.
Będzie przyjmować parametr n_sides (liczba boków)
i na jego podstawie tworzyć atrybut listy boków wielokatu (metoda input).

Z tej klasy dziedziczyc beda klasy Triangle, Rectangle, oraz Square.
Dla każdej z tych klas zaimplementuj metodę get_area, zwracającą polę danego wielokąta
"""

class Polygon:
    def __init__(self, n_sides) -> None:
        self.list_of_sides = [None] * n_sides

class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(n_sides=3)

class Rectangle(Polygon):
    def __init(self, a, b):
        super().__init__(n_sides=2)

class Square(Polygon):
    pass
