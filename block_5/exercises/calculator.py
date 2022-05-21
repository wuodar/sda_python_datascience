"""
    Stwórz klasę Calculator, w ktorej zaimplementujesz dzialania:
    - dodawanie,
    - odejmowanie,
    - mnozenie,
    - dzielenie.

    kalkulator am działać na dwóch zmiennych, a, b
"""


class Calculator:

    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b