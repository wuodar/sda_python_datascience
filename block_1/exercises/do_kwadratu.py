"""
    Napisz program, który poprosi użytkownika o liczbę naturalną (N) i wypisze wszystkie liczby
    od 1 do N podniesione do kwadratu (pętla for).

    Przyklad
        input:
            N = 5
        output:
            1
            4
            9
            16
            25
"""

N = input("Podaj liczbe naturalną: ") # pobieramy wartość od użytkownika
N = int(N) # ponieważ funkcja input() zwraca string, musimy p[rzekonwertować tą wartość na int (liczba całkowita)

for i in range(1, N+1): # iterujemy po elementach z zakresu [1, N+1) z krokiem 1
    print(i**2) # printujemy wartość i**2, operator ** oznacza potęgowanie, 2 oznacza stopień drugi potęgi
