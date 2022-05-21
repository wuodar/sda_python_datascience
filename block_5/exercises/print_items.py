"""
Napisz program, który będzie przyjmowała od użytkownika imię i nazwisko,
A następnie, do momemntu kiedy uzytkownik nie wprowadzi wartości "0", pobiera imiona
jego zwierząt (input), a następnie napisz funkcję która będzie jako parametr przyjmowałą to imię i nazwisko,
oraz dowolną liczbę nazw zwierząt, które dana osoba posiada. Funkcja ma wyprintować imię osoby
Oraz w każdej kolejnej linii imię jego zwierząt.

*args - reprezentowane przez klasę tupla - co za tym idzie, możemy sobie do tupli skonwertować
na przykład listę.
"""

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
