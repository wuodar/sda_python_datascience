"""
Napisz program, który będzie przyjmowała od użytkownika imię i nazwisko,
A następnie, do momemntu kiedy uzytkownik nie wprowadzi wartości "0", pobiera imiona
jego zwierząt (input), a następnie napisz funkcję która będzie jako parametr przyjmowałą to imię i nazwisko,
oraz dowolną liczbę nazw zwierząt, które dana osoba posiada. Funkcja ma wyprintować imię osoby
Oraz w każdej kolejnej linii imię jego zwierząt.
*args - reprezentowane przez klasę tupla - co za tym idzie, możemy sobie do tupli skonwertować
na przykład listę.
"""


first_name = input('Podaj swoje imię:')
last_name = input('Podaj swoje nazwisko:')

pets = []
while True:
    pet = input("Podaj imię zwierzątka. Jeżeli skończyłeś, wpisz \"0\": ")

    if pet == "0":
        break
    pets.append(pet)

# nagłówek ma zostać tak jak teraz
def print_name_and_pets(first_name, last_name, *pets):
    print(first_name, last_name)
    for i in pets:
        print(i)

print_name_and_pets(first_name, last_name, *pets)