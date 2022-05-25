"""
    Na podstawie klasy abstrakcyjnej Polygon, stworz 3 klasy dziedziczace: Square, Rectangle, Triangle.
    Kazda z tych klas musi byc konkretna (a nie abstrakcyjna), powinna wiec nadpisywac wszystkie metody
    abstrakcyjne z klasy Polygon. Kazda konkretna klasa powinna miec definicje konstruktora __init__
    (dla przykładu obiekt typu Square, powinien miec jeden atrybut self.side, obiekt rectabgle dwa atrybuty:
    self.side1, self.side2, a triangle self.side, self.height).
    Na koniec stworz funkcje zarzadzajaca obiektami stworzonych klas, ktora w petli bedzie obliczala pola
    dla kazdego obiektu
"""

from abc import ABC, abstractmethod
from typing import Union, List

# zaimportowana klasa ABC powoduje, że klasa Polygon jest abstrakcyjna
# to znaczy, ze nie możemy stworzyć obiektu tej klasy, służy tylko do dziedziczenia.
# dekorator @abstractmethod powoduje, że klasa dziedzicząca z klasy Polygon musi zawierać
# swoją implementację metody oznaczonej tym dekoratorem (calculate_area)
class Polygon(ABC):

    @abstractmethod
    def calculate_area(self) -> Union[int, float]:  # Union sugeruje ze funkcja moze zwrocic inta albo floata
        """Metoda ma za zadanie obliczyc pole danego obiektu.

        Ze wzgledu na fakt, iz nie wiemy w tym momencie jaki to jest wielokat,
        nie potrafimy obliczyc jego pola. Do redefinicji w klasie dziedziczacej.

        :return: wartosc pola jako liczba calkowita lub wymierna.
        """



class Square(Polygon):
    pass


class Rectangle(Polygon):
    pass


class Triangle(Polygon):
    pass

#  możemy zaanotować listę wielokątów jako List[Polygon], ponieważ każda klasa (Square, Ractangle, Triangle) dziedziczy
# z klasy polygon, zatem obiekty tych klas są zarazem instancjami klasy Polygon
def calculate_areas(polygons: List[Polygon]) -> List[float]:
    """Oblicza pola wszystkich wielokatow podanych w liscie.

    :param polygons: lista obiektow dziedziczacych po Polygon.
    :return: lista obliczonych pol.

    """
    pass


if __name__ == "__main__":
    square = Square(...)
    triangle = Triangle(...)
    rectangle = Rectangle(...)

    polygons = [square, triangle, rectangle]
    areas = calculate_areas(polygons)
    print(areas)