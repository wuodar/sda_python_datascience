# Zadanie numer 1
"""
Napisz program, który pobierze najpierw od użytkownika nazwę pliku,
do którego zapisane zostaną następnie dane pobrane od użytkownika.
Następnie, za każdym razem, kiedy użytkownik poda dane wejściowe,
wpisz go jako nowa linia do pliku, który utworzysz pod wskazaną nazwą.
Wpisywanie kończy się w momencie, kiedy użytkownik wpisze wartość 0.
"""
# 1. Pobranie od uzytkownika nazwy pliku
# 2. Stworzenie pliku przy użyciu kontekst menadżera
# 3. Pobranie pierwszej wartosci od uzytkownika
# 6. Pętla while z warunkiem, że input od uzytkownika jest rozny od 0
# 5. Dodajemy do pliku (przy czym należy pamiętać,
#  iż musimy dodać znak nowej liniii przy wpisywaniu)
# I do wpisania tego znaku nowej lini (\n)
# możemy wykorzystać np. fstring f"{variable}\n"

# ## moje rozwiązanie
# filename = input("Podaj nazwe: ")
#
# with open(filename, "w") as f:
#     user_input = input("Podaj dane: ", )
#     while user_input != "0":
#         f.write(f"{user_input}\n")
#         user_input = input("Podaj dane: ", )
#         if user_input == "0":
#             break
"""
Zadanie z chatu do przerobienia
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
"""
# Zadanie numer 2
"""
(Kontynuacja zadania numer 1)
Pobierz od użytkownika liczbę N,
Następnie pobierz od niego N wartości - w tym celu wykorzystaj 
list comprehensions, wynik przypisując do zmiennej.
Zapisz dane do pliku 'values.txt' przy użyciu funkcji writelines()
"""
#1. Pobranie od użytkownika nazwy pliku
#2. Stworzenie w kontekst menadzerze
#3. Pobierac od uzytkownika do momentu uzyskania 0:
#4. dodajemy do pliku, petla while z warunkiem i == 0, i- zmienna user input
#5. imput od uzytkownika jest rozny od zera
#6. otworzyc petle z tym warunkiem dodac do pliku
#7. w nastepnej petli pobieramy input od nowa, warunek się wywwali
#8. dodanie do pliku

"""
# file = open(
#     '/Users/dawidweber/PycharmProjects/KursDataScience/Python w Data Science/Zadania na zajęciach/values.txt',
#     'w')
# while True:
#     iteration_N = int(input("Podaj liczbę N: "))
#     file_data = [file.writelines(str(N+1)+'\n') for N in range(iteration_N)]
#     break
"""