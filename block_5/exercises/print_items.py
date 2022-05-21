"""
Napisz program, który będzie przyjmowała od użytkownika imię i nazwisko,
A następnie, do momemntu kiedy uzytkownik nie wprowadzi wartości "0", pobiera imiona
jego zwierząt (input), a następnie napisz funkcję która będzie jako parametr przyjmowałą to imię i nazwisko,
oraz dowolną liczbę nazw zwierząt, które dana osoba posiada. Funkcja ma wyprintować imię osoby
Oraz w każdej kolejnej linii imię jego zwierząt.
*args - reprezentowane przez klasę tupla - co za tym idzie, możemy sobie do tupli skonwertować
na przykład listę.
"""
first_name = input("Podaj imię: ")
last_name = input("Podaj nazwisko: ")
pets_list = []

# nagłówek ma zostać tak jak teraz
def print_name_and_pets(first_name, last_name, *pets):
        print(first_name, " ", last_name)
        for pet in pets_list:
            print(pet)


while True:
    pets = input("Podaj imię swojego zwierzaka, wciśnij 0 aby przerwać: ")
    pets_list.append(pets)
    if pets == "0":
        break

print_name_and_pets(first_name, last_name, pets_list)