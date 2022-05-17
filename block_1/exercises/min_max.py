"""
    Napisz program, który wyświetla
    najmniejszy i największy element listy, a także ją odwróci.

    Przykład
        input:
            input_list = [2, 3, 4, 5, 6, 7]
        output:
            min=2, max=7, reversed_list=[7, 6, 5, 4, 3, 2]
"""

input_list = [2, 3, 4, 5, 6, 7]

min_val = min(input_list) # funkcja wbudowana biblioteki standardowej pythona min, jako parametr przyjmuje obiekt Iterable (lista, set, tupla) i zwraca wartość minimalną
max_val = max(input_list) # funkcja max, działa tak jak funkcja min, z tą różnicą, że zwraca wartość maksymalną

reversed_iterator = reversed(input_list) # funkcja reversed przyjmuje jako parametr obiekt sekwencyjny (dict, list, tuple) i zwraca obiekt Iterable (który możemy przekonwertować do listy, setu, tupli), w przypadku dict'a, zwróci posortowane klucze
reversed_list = list(reversed_iterator) # ponieważ funkcja reversed() zwraca iterator, musimy go przekonwertować na listę

print("min=", min_val)
print("max=", max_val)
print("reversed list=", reversed_list)

