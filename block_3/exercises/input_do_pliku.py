# Zadanie numer 1
"""
Napisz program, który pobierze najpierw od użytkownika nazwę pliku,
do którego zapisane zostaną następnie dane pobrane od użytkownika.
Następnie, za każdym razem, kiedy użytkownik poda dane wejściowe,
wpisz go jako nowa linia do pliku, który utworzysz pod wskazaną nazwą.
Wpisywanie kończy się w momencie, kiedy użytkownik wpisze wartość 0.
"""

filename = input("Podaj nazwę pliku: ")
user_input = input("Podaj dane do wpisania do pliku: ")
with open(filename, "w") as file:
    while user_input != "0":
        file.write(f"{user_input}\n")
        user_input = input("Podaj kolejne dane do wpisania do pliku: ")

# Zadanie numer 2
"""
Pobierz od użytkownika liczbę N,
Następnie pobierz od niego N wartości - w tym celu wykorzystaj 
list comprehensions, wynik przypisując do zmiennej.
Zapisz dane do pliku 'values.txt' przy użyciu funkcji writelines()
"""

N = int(input("Podaj liczbę naturalną N: "))

inputs = [input(f"Podaj wartość numer {i+1}: ") for i in range(N)]
with open("values.txt", "w") as file:
    file.writelines(inputs)
