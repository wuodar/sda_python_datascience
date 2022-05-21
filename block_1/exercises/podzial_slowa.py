""""
    Napisz program, który pobiera od użytkownika słowo, a następnie wyświetla słowo złożone z co drugiego
    znaku pobranego. W drugiej kolejności program powinien wyświetlić słowo z pozostałych liter.

    przykład:
    słowo: Jagiellonia
    zwrotka: Jgelna, ailoi
"""

word = input("Podaj słowo: ")  # input() służy do pobierania danych od użytkownika, zwraca te dane jako obiekt string

# wykorzystujemy tzw. slicing, czyli wybieramy elementy z list wg. wzoru [start:stop:krok]
# jeśli chcemy iterować od pierwszego elementu z listy, możemy pominąć parametr start,
# jeśli chcemy iterować do ostatniego elementu z listy, możemy pominąć parametr stop
# podajemy zatem tylko parametr krok oraz start, ponieważ chcemy wyciągnąć co drugi znak z
# wejściowego string'a, do jednej zmiennej zaczynając od pierwsze elementu (dlatego start = 0)
# natomiast druga zmienna pobiera znaki od drugiego elementu (dlatego start = 1)
word_a = word[0::2]
word_b = word[1::2]
print(word_a, word_b)  # wyprintowanie wyniku
