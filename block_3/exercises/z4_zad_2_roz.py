"""# Zadanie numer 1
Napisz program, który pobierze najpierw od użytkownika nazwę pliku,
do którego zapisane zostaną następnie dane pobrane od użytkownika.
Następnie, za każdym razem, kiedy użytkownik poda dane wejściowe,
wpisz go jako nowa linia do pliku, który utworzysz pod wskazaną nazwą.
Wpisywanie kończy się w momencie, kiedy użytkownik wpisze wartość 0.

# 1. Pobranie od uzytkownika nazwy pliku
# 2. Stworzenie pliku przy użyciu kontekst menadżera
# 3. Pobranie pierwszej wartosci od uzytkownika
# 6. Pętla while z warunkiem, że input od uzytkownika jest rozny od 0
# 5. Dodajemy do pliku (przy czym należy pamiętać,
#  iż musimy dodać znak nowej liniii przy wpisywaniu)
# I do wpisania tego znaku nowej lini (\n)
# możemy wykorzystać np. fstring f"{variable}\n"
"""

import os
def write_to_file(file_name, text):

    with open(file_name, 'a') as file:
        if os.stat(file_name).st_size == 0:
            file.write(text)
        else:
            text = "\n" + text
            file.write(text)

name = input("Podaj nazwę pliku: ")

while True:
    sentence = input("Podaj tekst, który pragniesz dodać. Jeżeli skończyłeś, wpisz \"0\": ")
    if sentence == "0":
        break
    else:
        write_to_file(name, sentence)
"""# Zadanie numer 2
(Kontynuacja zadania numer 1)
Pobierz od użytkownika liczbę N,
Następnie pobierz od niego N wartości - w tym celu wykorzystaj 
list comprehensions, wynik przypisując do zmiennej.
Zapisz dane do pliku 'values.txt' przy użyciu funkcji writelines()
"""

def write_lines(N):
    file_name = input("Podaj nazwę pliku: ")
    file_data = []
    while True:
        value = input("Podaj dane wejściowe: ")
        if value == "0":
            break
        file_data.append(value+"\n")
    with open(file_name, "w") as f:
        f.writelines(N)
        f.writelines(file_data)

def list_compr():
    n = input("Podaj liczbę N: ")
    n_value = [f"{input('Podaj liczbe: ')}\n" for i in range(int(n)) ]
    return n_value

write_lines(list_compr())
