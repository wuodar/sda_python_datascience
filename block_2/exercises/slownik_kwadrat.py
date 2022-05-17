"""
     Napisz program, który pobiera od użytkownika liczbę N,
     następnie tworzy słownik z kluczami od 1 do N z wartościami,
     które są kwadratami kluczy.
"""

N = int(input("Podaj liczbe naturalna: "))

slownik = dict()
for i in range(1, N+1):
    slownik[i] = i**2

print(slownik)