# Styl zapisu zmiennych/funkcji/klas

# camelCase (Java) - np. isNumberGreaterThan10 (zmienna, funkcja), MyClass (klasa), ClassJWT
# zmienne globalne/pola klasy - MyVariable

# snake_case (Python) - np. is_number_greater_than_10 (zmienna, funckja),  MyClass (klasa), ClassJWT
# zmienne globalne/pola klasy - MY_VARIABLE

# argumenty domyślne nie mogą mieć po
# swojej prawej stronie parametrów bez wartości domyślnej
def func(param1, param2, param3="domyslna wartosc"):
    print(param1, param2, param3)


# func("1", "2")

# dodając gwaizdkę (*) przed nazwą parametru, powoodujemy
# że parametr staje się tuplą, i możęmy przekazać do naszej funkcji dowolną liczbę
# argumentów
def args_example(*container, param1, param2):
    print(type(container))
    for arg in container:
        print(arg)


#
# args_example("arg1", "arg2", "arg3", param1="arg4", param2="arg5")

def kwargs_example(**kwargs):
    print(type(kwargs))

    for k, v in kwargs.items():
        print(f"{k}: {v}")


some_dict = {"abc": "abc", "cde": "qwerty"}


# kwargs_example(**some_dict)
# function(param=value)


# type hinting


def add_integers(a: int, b: int) -> int:
    return a + b


val = add_integers(5, 5)


# print(val)

# -------- przykład customowej klasy zwracanej z funkcji

class SomeClass:
    pass


def return_some_object() -> SomeClass:
    return SomeClass()


# ------
def avg(*args: float, x: str = "some value") -> float:
    avg: float = sum(args) / len(args)
    print(x)
    return avg


# print(avg(1, 2, 3, 4, 5))


# ------------ moduły/importy
# importujemy klasę Car z modułu classes, podając do niego ścieżkę bezwzględną
# czyli od folderu głównego naszego projektu
from repo.block_4 import classes # classes to moduł, Car to klasa z modułu Classes

car = classes.Car("ERA CD12", "Opel", "Astra")
# print(car.manufacturer)

# import math
#
# sqrt_of_5 = math.sqrt(5)
# # print(sqrt_of_5)
#
# from math import sqrt
#
# sqrt_of_5 = sqrt(5)
# # print(sqrt_of_5)
#
# from math import sqrt as sqrt_renamed
#
# sqrt_of_5 = sqrt_renamed(5)
# # print(sqrt_of_5)

# nie powinno sie tak importowac (zła praktyka), bo nie kontrolujemy tego co jest zaimportowane z modułuj/biblioteki
from math import *
# użycie funkcji sqrt z biblioteki math
x = sqrt()

