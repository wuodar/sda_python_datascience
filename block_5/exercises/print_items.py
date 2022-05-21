"""
Napisz program, który będzie przyjmowała od użytkownika imię i nazwisko,
A następnie, do momemntu kiedy uzytkownik nie wprowadzi wartości "0", pobiera imiona
jego zwierząt (input), a następnie napisz funkcję która będzie jako parametr przyjmowałą to imię i nazwisko,
oraz dowolną liczbę nazw zwierząt, które dana osoba posiada. Funkcja ma wyprintować imię osoby
Oraz w każdej kolejnej linii imię jego zwierząt.

*args - reprezentowane przez klasę tupla - co za tym idzie, możemy sobie do tupli skonwertować
na przykład listę.
"""

# # nagłówek ma zostać tak jak teraz
# def print_name_and_pets(first_name, last_name, *pets):
#     print(first_name, last_name, pets)
#
# print_name_and_pets("Laura", "Kowalska", "kot", "kotka", "Fruzia")

first_name = input('Podaj swoje imię:')
last_name = input('Podaj swoje nazwisko:')


#pets = input('Podaj swoje zwierzaki:')
pets = []
while True:
    pet = input("Jeżeli skończyłeś, wpisz \"0\": ")
    if pet == "0":
        break
    #else:
        #continue
    pets.append(pet)
        #sentence =sentence + sentence


# nagłówek ma zostać tak jak teraz
def print_name_and_pets(first_name, last_name, *pets):
    print(first_name, last_name)
    #for

    #pass

print_name_and_pets(first_name, last_name, *pets) #*rozpakowuje liste przy wywołaniu
#print_name_and_pets("Laura", "Kowalska", "chomik", "jaszczur", "krowa")
