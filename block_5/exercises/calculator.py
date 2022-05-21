"""
    Stwórz klasę Calculator, w ktorej zaimplementujesz dzialania:
    - dodawanie,
    - odejmowanie,
    - mnozenie,
    - dzielenie.

    kalkulator am działać na dwóch zmiennych, a, b
"""


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def division(a,b):
        return a / b

print(Calculator.multiply(4,5))