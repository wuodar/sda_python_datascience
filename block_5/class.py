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
# def args_example(*container, param1, param2):
#     print(type(container))
#     for arg in container:
#         print(arg)
#
# args_example("arg1", "arg2", "arg3", param1="arg4", param2="arg5")






