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

<<<<<<< HEAD
# git stash, a potem git stash apply.

name = input("Podaj imię: ") or "Giovanni"
surname = input("Podaj naziwsko: ") or "Giorgio"
pets_names = list()

while True:
    temp = input("Podaj nazwę zwierzątka. Jeżeli chcesz zakończyć, wciśnij 0: ")
    if temp == "0":
        break
    else:
        pets_names.append(temp)


# nagłówek ma zostać tak jak teraz
def print_name_and_pets(first_name, last_name, *pets):
    print(f"{first_name} {last_name} ma zwierzątka o imionach:")

    for i in pets[0]:
        print(i)

print_name_and_pets(name, surname, pets_names)
=======
# imie = input()
# nazwisko = input()
# pets = []

# nagłówek ma zostać tak jak teraz
def print_name_and_pets(first_name, last_name, *pets):
    pass

# print_name_and_pets(imie, nazwisko, ...)
>>>>>>> main
