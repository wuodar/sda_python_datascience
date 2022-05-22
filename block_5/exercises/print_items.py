"""
Napisz program, który będzie przyjmowała od użytkownika imię i nazwisko i przypisze je do zmiennych,
A następnie, do momentu kiedy uzytkownik nie wprowadzi wartości "0", pobiera imiona
jego zwierząt (input) oraz również przypisze te imiona do zminnej (lista/tupla),
a następnie napisz funkcję która będzie jako parametr przyjmowałą to imię i nazwisko,
oraz dowolną liczbę nazw zwierząt, które dana osoba posiada. Funkcja ma wyprintować imię osoby
Oraz w każdej kolejnej linii imię jego zwierząt.

*args - reprezentowane przez klasę tupla - co za tym idzie, możemy sobie do tupli skonwertować
na przykład listę.
"""

first_name = input("Podaj imie: ")
last_name = input("Podaj nazwisko: ")
pets = []
while True:
    pet = input("Podaj zwierze: ")
    if pet == "0":
        break
    else:
        pets.append(pet)

# nagłówek ma zostać tak jak teraz
def print_name_and_pets(first_name, last_name, *pets): #
    print(f"{first_name} {last_name}")
    for pet in pets:
        print(pet)

print_name_and_pets(first_name, last_name, *pets)

