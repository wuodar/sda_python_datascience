"""
Stwórz klasę Polygon, która będzie reprezentować wielokąt.
Będzie przyjmować parametr n_sides (liczba boków)
i na jego podstawie tworzyć atrybut listy boków wielokatu (metoda input).

<<<<<<< HEAD
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
=======
Z tej klasy dziedziczyc beda klasy Triangle.
Zaimplementuj dla niej metodę get_area, zwracającą polę trójkąta
"""
# tutaj mamy import z biblioteki math, zadanko było dodatkowe, zatem wymagało dodatkowego wkładu.
# O bibliotekach (math to biblioteka) sobie jeszcze opowiemy :)
from math import sqrt


class Polygon:
    def __init__(self, n_sides):
        self.sides = [int(input(f"Podaj długość boku {i+1}: ")) for i in range(n_sides)]


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def get_area(self):
        """area of any triangle formula:
        https://www.cuemath.com/measurement/area-of-triangle/#:~:text=Area%20of%20Triangle%20Using%20Heron%27s%20Formula
        """
        s = sum(self.sides) / 2
        return sqrt(s * sum([s - side for side in self.sides]))


if __name__ == "__main__":
    triangle = Triangle()
    triangle_area = triangle.get_area()
    print(f"Area of triangle is equal to {triangle_area}")
>>>>>>> main
